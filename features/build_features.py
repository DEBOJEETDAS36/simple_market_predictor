import numpy as np
import pandas as pd
import os
from glob import glob

RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"

def create_processed_path():
    if not os.path.exists(PROCESSED_DATA_PATH):
        os.makedirs(PROCESSED_DATA_PATH)

def compute_returns(df):
    """Compute daily returns."""
    df['returns'] = df['price'].pct_change()
    return df

def compute_moving_averages(df):
     """Compute SMA indicators."""
     df["sma_10"] = df["close"].rolling(window=10).mean()
     df["sma_50"] = df["close"].rolling(window=50).mean()
     return df

def compute_volatility(df):
    """Rolling volatility."""
    df["volatility"] = df["returns"].rolling(window=10).std()
    return df

def compute_rsi(df, window=14):
    """
    Compute RSI (Relative Strength Index)
    """
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    df["rsi"] = 100 - (100 / (1 + rs))
    return df

def compute_momentum(df):
    """Simple momentum"""
    df["momentum"] = df["close"] - df["close"].shift(10)
    return df

def clean_data(df):
    """Drop NaNs after feature creation"""
    df = df.dropna()
    return df

def process_single_file(file_path):
    df = pd.read_csv(file_path)
    df = compute_returns(df)
    df = compute_moving_averages(df)
    df = compute_volatility(df)
    df = compute_rsi(df)
    df = compute_momentum(df)

    df = clean_data(df)

    return df

def process_all_stocks():
    create_processed_path()

    files = glob(os.path.join(RAW_DATA_PATH, "*.csv"))

    for file in files:
        df = process_single_file(file)

        ticker = os.path.basename(file).replace(".csv", "")
        output_path = os.path.join(PROCESSED_DATA_PATH, f"{ticker}.csv")

        df.to_csv(output_path, index=False)
        print(f"[INFO] Processed {ticker}")

if __name__ == "__main__":
    process_all_stocks()