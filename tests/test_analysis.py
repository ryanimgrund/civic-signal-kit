from __future__ import annotations

import tempfile
import unittest
from contextlib import redirect_stderr
from datetime import date
from io import StringIO
from pathlib import Path

from civic_signal_kit.analysis import DataPoint, classify_level, read_csv_points, summarize_points
from civic_signal_kit.cli import main, parse_thresholds


class SignalAnalysisTests(unittest.TestCase):
    def test_summarizes_latest_and_previous_windows(self) -> None:
        points = [
            DataPoint(date(2026, 5, 1), 10),
            DataPoint(date(2026, 5, 2), 20),
            DataPoint(date(2026, 5, 3), 30),
            DataPoint(date(2026, 5, 4), 40),
        ]

        summary = summarize_points(points, window=2, thresholds={"baseline": 0, "elevated": 25})

        self.assertEqual(summary.latest_value, 40)
        self.assertEqual(summary.rolling_average, 35)
        self.assertEqual(summary.previous_rolling_average, 15)
        self.assertAlmostEqual(summary.percent_change or 0, 133.3333333333)
        self.assertEqual(summary.direction, "increase")
        self.assertEqual(summary.level, "elevated")

    def test_classification_uses_highest_matching_threshold(self) -> None:
        level = classify_level(75, {"baseline": 0, "elevated": 25, "high": 50})

        self.assertEqual(level, "high")

    def test_reads_csv_points(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "data.csv"
            path.write_text("date,value\n2026-05-02,2\n2026-05-01,1\n", encoding="utf-8")

            points = read_csv_points(path, date_column="date", value_column="value")

        self.assertEqual([point.value for point in points], [1, 2])

    def test_summary_notes_missing_comparison_window_and_gaps(self) -> None:
        points = [
            DataPoint(date(2026, 5, 1), 10),
            DataPoint(date(2026, 5, 4), 20),
        ]

        summary = summarize_points(points, window=7)

        self.assertIn("No full previous comparison window is available.", summary.notes)
        self.assertTrue(any("Date gaps" in note for note in summary.notes))

    def test_parse_thresholds(self) -> None:
        self.assertEqual(parse_thresholds(["baseline=0", "high=50"]), {"baseline": 0.0, "high": 50.0})

    def test_cli_returns_error_for_bad_threshold(self) -> None:
        with redirect_stderr(StringIO()):
            result = main(["missing.csv", "--threshold", "bad"])

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
