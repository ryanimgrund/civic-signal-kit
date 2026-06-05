from __future__ import annotations

import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from io import StringIO
from pathlib import Path

from civic_signal_kit.analysis import DataPoint, classify_level, read_csv_points, summarize_points
from civic_signal_kit.cli import main, parse_thresholds
from civic_signal_kit.render import render_markdown


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
        self.assertEqual([threshold.name for threshold in summary.thresholds], ["baseline", "elevated"])

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

    def test_markdown_includes_reproducible_method(self) -> None:
        points = [
            DataPoint(date(2026, 5, 1), 10),
            DataPoint(date(2026, 5, 2), 20),
        ]

        markdown = render_markdown(summarize_points(points, window=2, thresholds={"baseline": 0}))

        self.assertIn("## Method", markdown)
        self.assertIn("Rolling window: 2 point(s)", markdown)
        self.assertIn("baseline>=0", markdown)

    def test_parse_thresholds(self) -> None:
        self.assertEqual(parse_thresholds(["baseline=0", "high=50"]), {"baseline": 0.0, "high": 50.0})

    def test_cli_returns_error_for_bad_threshold(self) -> None:
        with redirect_stderr(StringIO()):
            result = main(["missing.csv", "--threshold", "bad"])

        self.assertEqual(result, 2)

    def test_cli_writes_output_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = Path(tmp_dir) / "data.csv"
            output_path = Path(tmp_dir) / "summary.md"
            csv_path.write_text("date,value\n2026-05-01,10\n2026-05-02,20\n", encoding="utf-8")

            result = main([str(csv_path), "--window", "1", "--output", str(output_path)])

            self.assertEqual(result, 0)
            self.assertIn("# Signal Summary", output_path.read_text(encoding="utf-8"))

    def test_cli_can_fail_on_quality_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = Path(tmp_dir) / "data.csv"
            csv_path.write_text("date,value\n2026-05-01,10\n", encoding="utf-8")

            with redirect_stderr(StringIO()), redirect_stdout(StringIO()):
                result = main([str(csv_path), "--fail-on-notes"])

            self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
