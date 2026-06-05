from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, datetime
from math import isfinite
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class DataPoint:
    observed_on: date
    value: float


@dataclass(frozen=True)
class Threshold:
    name: str
    lower_bound: float

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "lower_bound": self.lower_bound,
        }


@dataclass(frozen=True)
class SignalSummary:
    latest_date: date
    latest_value: float
    rolling_average: float
    previous_rolling_average: float | None
    percent_change: float | None
    direction: str
    level: str
    window: int
    point_count: int
    thresholds: tuple[Threshold, ...]
    notes: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "latest_date": self.latest_date.isoformat(),
            "latest_value": self.latest_value,
            "rolling_average": self.rolling_average,
            "previous_rolling_average": self.previous_rolling_average,
            "percent_change": self.percent_change,
            "direction": self.direction,
            "level": self.level,
            "window": self.window,
            "point_count": self.point_count,
            "thresholds": [threshold.to_dict() for threshold in self.thresholds],
            "notes": list(self.notes),
        }


def summarize_csv(
    path: str | Path,
    *,
    date_column: str,
    value_column: str,
    window: int = 7,
    thresholds: dict[str, float] | None = None,
) -> SignalSummary:
    points = read_csv_points(path, date_column=date_column, value_column=value_column)
    return summarize_points(points, window=window, thresholds=thresholds)


def read_csv_points(path: str | Path, *, date_column: str, value_column: str) -> list[DataPoint]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = {date_column, value_column} - set(reader.fieldnames or [])
        if missing:
            names = ", ".join(sorted(missing))
            raise ValueError(f"Missing required column(s): {names}")

        points: list[DataPoint] = []
        for line_number, row in enumerate(reader, start=2):
            raw_date = (row.get(date_column) or "").strip()
            raw_value = (row.get(value_column) or "").strip()
            if not raw_date or not raw_value:
                continue
            try:
                points.append(DataPoint(parse_date(raw_date), float(raw_value)))
            except ValueError as exc:
                raise ValueError(f"Invalid data on CSV line {line_number}: {exc}") from exc

    return sorted(points, key=lambda point: point.observed_on)


def summarize_points(
    points: Iterable[DataPoint],
    *,
    window: int = 7,
    thresholds: dict[str, float] | None = None,
) -> SignalSummary:
    ordered = sorted(points, key=lambda point: point.observed_on)
    if not ordered:
        raise ValueError("At least one data point is required")
    if window < 1:
        raise ValueError("Window must be at least 1")

    latest_window = ordered[-window:]
    previous_window = ordered[-(window * 2) : -window]
    rolling_average = mean(point.value for point in latest_window)
    previous_average = mean(point.value for point in previous_window) if previous_window else None
    percent = percent_delta(previous_average, rolling_average)

    normalized_thresholds = normalize_thresholds(thresholds or default_thresholds())

    return SignalSummary(
        latest_date=ordered[-1].observed_on,
        latest_value=ordered[-1].value,
        rolling_average=rolling_average,
        previous_rolling_average=previous_average,
        percent_change=percent,
        direction=direction_for(percent),
        level=classify_normalized_level(rolling_average, normalized_thresholds),
        window=window,
        point_count=len(ordered),
        thresholds=normalized_thresholds,
        notes=tuple(data_quality_notes(ordered, window=window, has_previous_window=bool(previous_window))),
    )


def default_thresholds() -> dict[str, float]:
    return {
        "baseline": 0.0,
        "elevated": 25.0,
        "high": 50.0,
    }


def classify_level(value: float, thresholds: dict[str, float]) -> str:
    return classify_normalized_level(value, normalize_thresholds(thresholds))


def normalize_thresholds(thresholds: dict[str, float]) -> tuple[Threshold, ...]:
    if not thresholds:
        raise ValueError("At least one threshold is required")

    normalized: list[Threshold] = []
    for name, lower_bound in thresholds.items():
        clean_name = name.strip()
        if not clean_name:
            raise ValueError("Threshold name cannot be empty")
        if not isfinite(lower_bound):
            raise ValueError(f"Threshold '{clean_name}' must be a finite number")
        normalized.append(Threshold(clean_name, lower_bound))

    return tuple(sorted(normalized, key=lambda threshold: threshold.lower_bound))


def classify_normalized_level(value: float, thresholds: tuple[Threshold, ...]) -> str:
    level = thresholds[0].name
    for threshold in thresholds:
        lower_bound = threshold.lower_bound
        if value >= lower_bound:
            level = threshold.name
    return level


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%Y/%m/%d").date()


def mean(values: Iterable[float]) -> float:
    collected = list(values)
    if not collected:
        raise ValueError("Cannot calculate a mean from no values")
    return sum(collected) / len(collected)


def percent_delta(previous: float | None, current: float) -> float | None:
    if previous is None or previous == 0:
        return None
    return ((current - previous) / previous) * 100


def direction_for(percent_change: float | None) -> str:
    if percent_change is None:
        return "unknown"
    if percent_change > 5:
        return "increase"
    if percent_change < -5:
        return "decrease"
    return "stable"


def data_quality_notes(points: list[DataPoint], *, window: int, has_previous_window: bool) -> list[str]:
    notes: list[str] = []
    if len(points) < window:
        notes.append(f"Only {len(points)} point(s) available for a {window}-point rolling average.")
    if not has_previous_window:
        notes.append("No full previous comparison window is available.")

    duplicate_dates = len({point.observed_on for point in points}) != len(points)
    if duplicate_dates:
        notes.append("Duplicate dates are present; values were not aggregated before analysis.")

    gaps = [
        (later.observed_on - earlier.observed_on).days
        for earlier, later in zip(points, points[1:])
    ]
    if any(gap > 1 for gap in gaps):
        notes.append("Date gaps are present; rolling averages use available rows, not calendar-filled values.")

    return notes
