# Contributing

Thanks for helping improve Civic Signal Kit.

## Principles

- Keep assumptions visible.
- Prefer plain language over technical flourish.
- Avoid advice. Summarize data and explain thresholds.
- Keep dependencies minimal.
- Add tests for calculations and rendering changes.
- Treat civic and public-health data as sensitive even when it is public.

## Local Setup

```sh
python -m pip install -e .
python -m unittest discover -s tests
```

## Pull Request Checklist

- The change has a clear user or maintainer benefit.
- Tests pass with `python -m unittest discover -s tests`.
- Threshold or calculation changes are documented.
- New output text is plain and non-alarmist.
- No analytics, tracking, or remote logging is added.

## Good First Issues

- Add sample datasets under `docs/examples`.
- Add missing-data warnings.
- Add chart export.
- Add localized render templates.
- Add more CLI examples.
