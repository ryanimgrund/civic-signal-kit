# PyPI Publishing

Civic Signal Kit is published on PyPI:

https://pypi.org/project/civic-signal-kit/

The repository uses a tokenless GitHub Actions workflow at `.github/workflows/publish.yml`.

Use PyPI Trusted Publishing instead of a password or API token.

## Trusted Publisher Values

The PyPI trusted publisher uses these values:

- PyPI project name: `civic-signal-kit`
- Owner: `ryanimgrund`
- Repository name: `civic-signal-kit`
- Workflow name: `publish.yml`
- Environment name: `pypi`

Keep passwords and tokens out of the repository. Never paste them into issues, docs, commits, or chat logs.

## Build And Check

From the repository root:

```sh
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

## Publish

For future releases, update the package version, create the GitHub Release or tag, and run the `Publish to PyPI` workflow from GitHub Actions.

## After Publishing

- Keep the PyPI URL in the GitHub repository website field.
- Keep installation instructions current in `README.md`.
- Track download metrics honestly. Do not claim downloads until PyPI reports them.
- Link the PyPI package from applications and release notes only when the package version is live.
