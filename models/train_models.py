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

def train_test_split_time_series(df, split_ratio=0.8):
    """
    Time-series aware split.
    No shuffling.
    """
    split_ratio = int(len(df) * split_ratio)
    train_df = df.iloc[:split_ratio]
    test_df = df.iloc[split_ratio:]

    return train_df, test_df

def train_model(X_train, y_train):
    """
    Train XGBoost classifier
    """
    model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42
    )
    
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.
    """
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)

    print("\n===== MODEL PERFORMANCE =====")
    print(f"Accuracy: {acc:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
