# ⚙️ Feature Engineering

## Purpose

Transform raw OHLCV data into model-ready signals.

## Features Created

### Returns

* Percentage change in closing price

### Moving Averages

* sma_10 → short-term trend
* sma_50 → long-term trend

### Volatility

* Rolling standard deviation of returns

### RSI

* Momentum indicator (0–100)

### Momentum

* Price difference over 10 days

## Notes

* Rolling windows introduce NaNs
* These rows are dropped in cleaning step

## Output

Saved in data/processed/
