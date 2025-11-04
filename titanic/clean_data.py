import pandas as pd
import numpy as np

# ---------------------------------
# 1. Missing Data Summary
# ---------------------------------
def summarise_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarise missing values in a DataFrame.
    Returns total count, percent missing, and column dtypes.
    """
    total = df.isnull().sum()
    percent = (total / df.shape[0]) * 100
    types = df.dtypes.astype(str)
    summary = pd.concat([total, percent, types], axis=1, keys=["Total", "Percent", "Type"])
    return summary.T


# ---------------------------------
# 2. Most Frequent Values
# ---------------------------------
def summarise_frequent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarise the most frequent value and its frequency (%) for each column.
    """
    total = df.count()
    items, freqs = [], []
    for col in df.columns:
        try:
            top_item = df[col].value_counts().index[0]
            top_freq = df[col].value_counts().values[0]
        except Exception:
            top_item, top_freq = np.nan, 0
        items.append(top_item)
        freqs.append(top_freq)
    summary = pd.DataFrame({
        "Most frequent item": items,
        "Frequency": freqs,
        "Percent from total": np.round(np.array(freqs) / total * 100, 3)
    }, index=df.columns)
    return summary.T


# ---------------------------------
# 3. Unique Values
# ---------------------------------
def summarise_uniques(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarise the count of unique values for each column.
    """
    uniques = df.nunique()
    summary = pd.DataFrame({"Total": df.count(), "Uniques": uniques}).T
    return summary


# ---------------------------------
# 4. Main Cleaning Function
# ---------------------------------
def clean_titanic_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Titanic dataset: handle missing data, drop irrelevant columns,
    and encode categorical variables.
    """
    df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], errors="ignore")
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1}).astype(int)
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)
    return df
