# Pilot Plan

This project needs real usage evidence before it should be described as broadly adopted. The goal of the pilot plan is to gather that evidence honestly.

## Candidate Pilot Users

- Educators teaching public data literacy.
- Journalists working with recurring public CSV exports.
- Community groups tracking service demand or attendance.
- Civic volunteers who need transparent summaries but do not have engineering support.

## Pilot Checklist

1. Identify one non-sensitive CSV dataset with a date column and one numeric value column.
2. Define thresholds with the user and document who chose them.
3. Run the CLI with Markdown and JSON output.
4. Ask the user whether the summary is understandable, reproducible, and cautious enough.
5. Record issues as public GitHub issues when they do not expose sensitive data.
6. Release small fixes with changelog notes and linked issues.

## Evidence To Collect

- Public issues from testers.
- Pull requests or documented maintainer responses.
- GitHub releases tied to changelog entries.
- PyPI publication and download metrics if the package is published.
- Examples based on public, non-sensitive datasets.

## Boundaries

Do not claim downloads, users, deployments, or institutional adoption until there is evidence. Do not use private health, student, client, or service-user data in public examples.
