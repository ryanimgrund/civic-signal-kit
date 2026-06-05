# Recommended GitHub Repository Settings

These settings improve discoverability and maintainer trust. They need to be set in GitHub because they are repository metadata, not files.

## Description

Transparent trend summaries for public-interest CSV time-series data.

## Website

Leave blank until documentation is published.

After PyPI publication, use the PyPI project URL.

## Topics

- civic-tech
- public-interest
- data-analysis
- time-series
- python
- csv
- risk-communication
- open-source

## Features

- Issues: enabled
- Discussions: enabled when there are real users or testers
- Projects: optional
- Wiki: disabled unless it is actively maintained

## Releases

- Create a GitHub Release for `v0.2.0`.
- Use `docs/releases/v0.2.0.md` as the release body.
- Mark it as the latest release.

## Branch Protection

When there is more than one contributor:

- Require pull requests before merging.
- Require CI to pass.
- Require conversation resolution.
- Protect the `main` branch from force pushes.
