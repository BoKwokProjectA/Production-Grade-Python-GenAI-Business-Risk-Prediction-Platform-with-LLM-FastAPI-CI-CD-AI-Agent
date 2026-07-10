"""
Feature engineering for skin lesion analysis
"""

import pandas as pd


def feature_engineering_new(df: pd.DataFrame, version: str = "v7"):
    """Apply feature engineering to the dataset"""
    df = df.copy()
    if "age_approx" in df.columns:
        df["age_approx"] = df["age_approx"].fillna(50)
    if "patient_id" in df.columns:
        df["count_per_patient"] = df.groupby("patient_id")["patient_id"].transform("count")
    return df


def preprocess_df(train, test, feature_cols, cat_cols):
    """Preprocessing for train and test data"""
    return train, test, feature_cols, cat_cols


print("✅ feature_engineering.py recreated successfully!")
