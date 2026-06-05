# Security Policy

## Supported Versions

Civic Signal Kit is pre-1.0. Security fixes are applied to the `main` branch until tagged releases begin.

## Reporting a Vulnerability

Please do not open a public issue for a vulnerability. Use GitHub private vulnerability reporting if enabled, or contact the maintainer through GitHub.

Useful reports include:

- Summary of the issue.
- Steps to reproduce.
- Impact.
- Suggested fix, if known.

## Security Scope

This project is a local CLI/library. Current priorities are:

- No remote logging.
- No analytics or tracking.
- Safe CSV parsing errors.
- Clear handling of malformed input.
- No hidden network calls.
