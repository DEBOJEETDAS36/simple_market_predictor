import yfinance as yf
import pandas as pd
import os
from datetime import datetime

DATA_DIR = "data/raw"

def create_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def fetch_stock_data(ticker, start="2020-01-01", end=None):
    """
    Fetch historical OHLCV data for a given stock.

    Args:
        ticker (str): Stock ticker (e.g., AAPL, RELIANCE.NS)
        start (str): Start date
        end (str): End date

    Returns:
        pd.DataFrame: Stock data
    """
    if end is None:
        end = datetime.today().strftime('%Y-%m-%d')

    df = yf.download(ticker, start=start, end=end, progress=False)

    df.reset_index(inplace=True)
    df['Ticker'] = ticker

    return df

