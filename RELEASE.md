# Release Checklist

1. Run tests:

   ```sh
   python -m unittest discover -s tests
   ```

2. Run the example commands from [docs/examples](docs/examples).
3. Update `CHANGELOG.md`.
4. Update the version in `pyproject.toml` and `CITATION.cff`.
5. Create a signed or clearly named git tag, for example `v0.1.0`.
6. Publish the GitHub release with:
   - summary of user-facing changes
   - testing notes
   - known limitations
   - privacy/security notes
7. Publish to PyPI when package ownership is configured.
8. Open follow-up issues for any known release gaps.
