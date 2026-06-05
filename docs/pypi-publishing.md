# PyPI Publishing

This project is not published to PyPI yet. The repository includes a tokenless GitHub Actions workflow at `.github/workflows/publish.yml`.

Use PyPI Trusted Publishing instead of a password or API token.

## Pending Publisher Values

Create a pending publisher on PyPI with these exact values:

- PyPI project name: `civic-signal-kit`
- Owner: `ryanimgrund`
- Repository name: `civic-signal-kit`
- Workflow name: `publish.yml`
- Environment name: `pypi`

After the pending publisher exists, run the `Publish to PyPI` workflow manually from GitHub Actions. The first successful run should create the PyPI project.

## One-Time Setup

1. Create or sign in to a PyPI account.
2. Enable two-factor authentication.
3. Add the pending publisher values above.
4. Keep passwords and tokens out of the repository. Never paste them into issues, docs, commits, or chat logs.

## Build And Check

From the repository root:

```sh
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

## Publish

After the pending publisher is configured, run the `Publish to PyPI` workflow from GitHub Actions.

## After Publishing

- Add the PyPI URL to the GitHub repository website field.
- Add installation instructions to `README.md`.
- Track download metrics honestly. Do not claim downloads until PyPI reports them.
- Link the PyPI package from the OpenAI application only after it is live.
