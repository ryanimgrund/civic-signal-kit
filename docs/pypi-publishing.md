# PyPI Publishing

This project is not published to PyPI yet. Publish only after the GitHub repository metadata and `v0.2.0` GitHub Release are in place.

## One-Time Setup

1. Create or sign in to a PyPI account.
2. Enable two-factor authentication.
3. Create a scoped API token for the `civic-signal-kit` project after the first upload, or use a trusted publishing workflow later.
4. Keep tokens out of the repository. Never paste them into issues, docs, commits, or chat logs.

## Build And Check

From the repository root:

```sh
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

## Publish

Use TestPyPI first:

```sh
python -m twine upload --repository testpypi dist/*
```

Then publish to PyPI:

```sh
python -m twine upload dist/*
```

## After Publishing

- Add the PyPI URL to the GitHub repository website field.
- Add installation instructions to `README.md`.
- Track download metrics honestly. Do not claim downloads until PyPI reports them.
- Link the PyPI package from the OpenAI application only after it is live.
