from __future__ import annotations

import argparse
import sys

from .analysis import summarize_csv
from .render import render_json, render_markdown


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        thresholds = parse_thresholds(args.threshold)
        summary = summarize_csv(
            args.csv_path,
            date_column=args.date_column,
            value_column=args.value_column,
            window=args.window,
            thresholds=thresholds,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(render_json(summary), end="")
    else:
        print(render_markdown(summary), end="")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="civic-signal",
        description="Summarize a public-interest time series from CSV.",
    )
    parser.add_argument("csv_path", help="Path to the CSV file.")
    parser.add_argument("--date-column", default="date", help="Date column name. Defaults to date.")
    parser.add_argument("--value-column", default="value", help="Numeric value column name. Defaults to value.")
    parser.add_argument("--window", type=int, default=7, help="Rolling window size. Defaults to 7.")
    parser.add_argument(
        "--threshold",
        action="append",
        default=[],
        metavar="NAME=VALUE",
        help="Inclusive lower-bound threshold. Can be repeated.",
    )
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    return parser


def parse_thresholds(values: list[str]) -> dict[str, float] | None:
    if not values:
        return None

    thresholds: dict[str, float] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"Invalid threshold '{value}'. Expected NAME=VALUE.")
        name, raw_number = value.split("=", 1)
        name = name.strip()
        if not name:
            raise ValueError("Threshold name cannot be empty")
        try:
            thresholds[name] = float(raw_number)
        except ValueError as exc:
            raise ValueError(f"Invalid threshold value for '{name}': {raw_number}") from exc
    return thresholds
