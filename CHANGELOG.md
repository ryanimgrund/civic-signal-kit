# Changelog

All notable changes to Civic Signal Kit will be documented here.

## 0.2.0 - 2026-06-05

- Added threshold metadata to JSON output and Markdown method notes.
- Added `--output` for writing summaries to files in recurring workflows.
- Added `--fail-on-notes` so data-quality notes can fail automated checks.
- Expanded tests for reproducible methods, output files, and quality-gate exit codes.
- Updated README examples to show reproducible thresholds and report artifact output.

## 0.1.0 - 2026-06-05

- Initial local CLI and Python package.
- Added CSV reading, rolling averages, comparison windows, threshold classification, Markdown output, and JSON output.
- Added data-quality notes for short histories, missing comparison windows, duplicate dates, and date gaps.
- Added synthetic examples for wastewater and air quality signals.
- Added tests, CI, privacy notes, security policy, issue templates, and maintainer documentation.
