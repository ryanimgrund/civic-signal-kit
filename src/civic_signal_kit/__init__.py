"""Transparent trend summaries for public-interest time-series data."""

from .analysis import SignalSummary, Threshold, summarize_csv, summarize_points

__all__ = ["SignalSummary", "Threshold", "summarize_csv", "summarize_points"]
