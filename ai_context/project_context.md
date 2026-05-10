# 🧠 AI Context (Day 1)

## What exists

* Data ingestion pipeline
* Raw OHLCV stock data

## Key Module

data_pipeline/fetch_data.py

## What is NOT built yet

* Features
* Models
* Sentiment
* Backtesting

## How data is structured

Each ticker has its own CSV file in data/raw/

## Next Step

Feature engineering module will transform raw data into model-ready features.

## Day 2 Update

### New Module

features/build_features.py

### Features Available

* returns
* RSI
* moving averages
* volatility
* momentum

### Data Flow Now

Raw Data → Features → (next: models)

### Next Step

Train ML models on processed dataset.
