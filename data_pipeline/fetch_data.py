import yfinance as yf
import pandas as pd
import os
from datetime import datetime
from tqdm import tqdm

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

def save_data(df, ticker):
    """
    Save stock data to CSV.

    Args:
        df (pd.DataFrame): Stock data
        ticker (str): Stock ticker
    """
    file_path = os.path.join(DATA_DIR, f"{ticker}.csv")
    df.to_csv(file_path, index=False)


def fetch_multiple_stocks(tickers):
    """
    Fetch data for multiple stocks.

    Args:
        tickers (list): List of stock tickers
    """
    create_data_dir()
    for ticker in tqdm(tickers):
        df = fetch_stock_data(ticker)
        if df is not None:
            save_data(df, ticker)

