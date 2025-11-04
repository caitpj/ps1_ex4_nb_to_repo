import pandas as pd
from pathlib import Path

def load_train_data(path: str | Path) -> pd.DataFrame:
    """
    Load Titanic training data.
    """
    path = Path(path)
    df = pd.read_csv(path)
    print(f"Loaded training data: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def load_test_data(path: str | Path) -> pd.DataFrame:
    """
    Load Titanic test data.
    """
    path = Path(path)
    df = pd.read_csv(path)
    print(f"Loaded test data: {df.shape[0]} rows × {df.shape[1]} columns")
    return df

