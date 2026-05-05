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

