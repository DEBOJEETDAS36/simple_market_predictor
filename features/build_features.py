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