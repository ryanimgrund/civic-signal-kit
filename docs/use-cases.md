# Use Cases

Civic Signal Kit is for small public-interest teams that already have simple CSV time-series data and need a reproducible way to explain recent movement.

## Community Reporting

Journalists and civic volunteers can summarize recurring public datasets while keeping thresholds, windows, and data-quality caveats visible in the published note.

## Public Health Communication

Public-health communicators can produce plain-language summaries for signals such as synthetic wastewater examples, service demand, or clinic attendance. The toolkit does not provide medical advice; it documents what changed in the data.

## Education

Educators can use the examples to teach rolling averages, threshold classification, and responsible uncertainty language without requiring cloud services or heavy dependencies.

## Internal Monitoring

Small nonprofits or civic teams can run the CLI on scheduled CSV exports and use `--fail-on-notes` to block publication when the input has gaps, duplicate dates, or too little history.

## Not In Scope

- Emergency alerts.
- Medical, legal, financial, or operational advice.
- Automated publication without human review.
- Hidden thresholds or undocumented scoring.
