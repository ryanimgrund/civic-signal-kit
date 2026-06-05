"""Transparent trend summaries for public-interest time-series data."""

from .analysis import SignalSummary, summarize_csv, summarize_points

__all__ = ["SignalSummary", "summarize_csv", "summarize_points"]
