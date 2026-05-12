import pandas as pd
import os
from glob import glob
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
import joblib

PROCESSED_DATA_PATH = "data/processed"
MODEL_SAVE_PATH = "saved_models"

FEATURE_COLUMNS = [
    "returns",
    "sma_10",
    "sma_50",
    "volatility",
    "rsi",
    "momentum"
]

def create_target(df):
    """
    Create binary target:
    1 = next day price up
    0 = next day price down
    """
    df["future_return"] = df["close"].shift(-1) - df["close"]
    df["target"] = (df["future_return"] > 0).astype(int)

    return df

