# Civic Signal Kit

Civic Signal Kit is a small Python toolkit for turning plain CSV time-series data into transparent public-interest trend summaries.

It is designed for educators, journalists, community groups, public-health communicators, and civic volunteers who need to explain what changed in a dataset without hiding the assumptions.

The toolkit does not give medical, legal, financial, or emergency advice. It summarizes data and exposes the thresholds used for classification.

## What It Does

- Reads a CSV with a date column and a numeric value column.
- Calculates rolling averages.
- Compares the latest period with the previous period.
- Classifies the latest value using user-provided thresholds.
- Flags simple data-quality issues such as short histories, duplicate dates, and date gaps.
- Exports a plain-language Markdown or JSON summary.
- Uses only the Python standard library.

## Example

Input CSV:

```csv
date,value
2026-05-01,12
2026-05-02,14
2026-05-03,16
2026-05-04,20
2026-05-05,22
2026-05-06,24
2026-05-07,26
2026-05-08,31
2026-05-09,34
2026-05-10,38
```

Command:

```sh
python -m civic_signal_kit sample.csv --date-column date --value-column value --format markdown
```

Output:

```md
# Signal Summary

- Latest date: 2026-05-10
- Latest value: 38.00
- 7-point rolling average: 27.86
- Previous 7-point rolling average: 20.00
- Change: 39.29% increase
- Level: elevated
```

## Install for Local Development

```sh
python -m pip install -e .
python -m unittest discover -s tests
```

## CLI

```sh
python -m civic_signal_kit path/to/data.csv \
  --date-column date \
  --value-column value \
  --window 7 \
  --threshold baseline=0 \
  --threshold elevated=25 \
  --threshold high=50 \
  --format markdown
```

Thresholds are inclusive lower bounds. The highest threshold less than or equal to the latest rolling average becomes the level.

## Examples

Runnable sample CSVs live in [docs/examples](docs/examples).

```sh
python -m civic_signal_kit docs/examples/wastewater-signal.csv \
  --date-column date \
  --value-column concentration \
  --threshold baseline=0 \
  --threshold elevated=250 \
  --threshold high=500
```

## Project Values

- Transparent assumptions.
- Plain language.
- No hidden dependencies.
- No analytics, tracking, or remote logging.
- Useful defaults, but user-owned thresholds.

## Roadmap

- Add examples for wastewater, air quality, attendance, and service-demand data.
- Add chart export.
- Add localization-friendly message templates.
- Expand validation reports for messy CSVs.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
