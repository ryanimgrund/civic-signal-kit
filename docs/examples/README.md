# Examples

These example CSVs are synthetic. They are intended for documentation and tests, not for real-world decisions.

## Wastewater Signal

```sh
python -m civic_signal_kit docs/examples/wastewater-signal.csv \
  --date-column date \
  --value-column concentration \
  --threshold baseline=0 \
  --threshold elevated=250 \
  --threshold high=500
```

## Air Quality Signal

```sh
python -m civic_signal_kit docs/examples/air-quality.csv \
  --date-column date \
  --value-column pm25 \
  --threshold good=0 \
  --threshold moderate=12 \
  --threshold unhealthy=35
```
