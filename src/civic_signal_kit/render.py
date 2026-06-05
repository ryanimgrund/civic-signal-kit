from __future__ import annotations

import json

from .analysis import SignalSummary


def render_json(summary: SignalSummary) -> str:
    return json.dumps(summary.to_dict(), indent=2, sort_keys=True) + "\n"


def render_markdown(summary: SignalSummary) -> str:
    change = "not available"
    if summary.percent_change is not None:
        change = f"{abs(summary.percent_change):.2f}% {summary.direction}"

    previous = "not available"
    if summary.previous_rolling_average is not None:
        previous = f"{summary.previous_rolling_average:.2f}"

    return "\n".join(
        [
            "# Signal Summary",
            "",
            f"- Latest date: {summary.latest_date.isoformat()}",
            f"- Latest value: {summary.latest_value:.2f}",
            f"- {summary.window}-point rolling average: {summary.rolling_average:.2f}",
            f"- Previous {summary.window}-point rolling average: {previous}",
            f"- Change: {change}",
            f"- Level: {summary.level}",
            f"- Data points used: {summary.point_count}",
            "",
            "This is a data summary, not advice. Review source quality and thresholds before using it for decisions.",
            "",
        ]
    )
