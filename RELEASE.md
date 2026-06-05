# Release Checklist

1. Run tests:

   ```sh
   python -m pip install -e .
   python -m unittest discover -s tests
   ```

2. Run the example commands from [docs/examples](docs/examples).
3. Update `CHANGELOG.md`.
4. Update the version in `pyproject.toml` and `CITATION.cff`.
5. Create a signed or clearly named git tag, for example `v0.2.0`.
6. Publish the GitHub release with:
   - summary of user-facing changes
   - testing notes
   - known limitations
   - privacy/security notes
7. Use the prepared release notes in `docs/releases/v0.2.0.md` when publishing `v0.2.0`.
8. Confirm the PyPI pending publisher is configured as described in `docs/pypi-publishing.md`.
9. Run the `Publish to PyPI` workflow from GitHub Actions.
10. Open follow-up issues for any known release gaps.
