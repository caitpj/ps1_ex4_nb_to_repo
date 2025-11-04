from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report
import pandas as pd
import os
from typing import List, Tuple

def encode_sex(df):
    """Convert 'Sex' to numeric (female=1, male=0) with robust cleaning."""
    if "Sex" not in df.columns:
        return df
    s = (df["Sex"]
         .astype("string").str.strip().str.lower()
         .map({"female": 1, "male": 0}))          # -> may produce NaNs
    if s.isna().any():                             # fill any unknown/missing with mode
        fill_val = s.mode().iloc[0] if not s.mode().empty else 0
        s = s.fillna(fill_val)
    df["Sex"] = s.astype(int)
    return df


def make_train_valid_xy(
    train: pd.DataFrame,
    valid: pd.DataFrame,
    predictors: List[str],
    target: str
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """Return (train_X, train_Y, valid_X, valid_Y) for modelling."""
    train_X = train[predictors]
    train_Y = train[target]
    valid_X = valid[predictors]
    valid_Y = valid[target]
    return train_X, train_Y, valid_X, valid_Y


def fit_rf_and_predict(train_X, train_Y, valid_X,
                       n_estimators=100, criterion="gini",
                       random_state=42, n_jobs=-1, verbose=False):
    """
    Initialise RandomForest, fit on (train_X, train_Y),
    and return (clf, preds_train, preds_valid).
    """
    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        criterion=criterion,
        random_state=random_state,
        n_jobs=n_jobs,
        verbose=verbose
    )
    clf.fit(train_X, train_Y)
    preds_tr = clf.predict(train_X)
    preds_va = clf.predict(valid_X)
    return clf, preds_tr, preds_va

def evaluate_classification(train_Y, preds_tr, valid_Y, preds_va):
    """
    Print classification reports for train and validation predictions.
    """
    print("=== Classification report: TRAIN ===")
    print(classification_report(train_Y, preds_tr, target_names=["Not Survived", "Survived"]))
    print("\n=== Classification report: VALIDATION ===")
    print(classification_report(valid_Y, preds_va, target_names=["Not Survived", "Survived"]))

def predict_and_export(model, test_df, features, out_path="submissions/rf_baseline.csv",
                       id_col="PassengerId", id_series=None):
    """
    Predict on test_df[features] and write Kaggle CSV.
    If PassengerId got dropped, pass id_series=test_raw[id_col] or keep id_col in test_df.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    X_test = test_df[features]
    preds = model.predict(X_test).astype(int)

    # get IDs: prefer explicit series, else column, else index if named correctly
    if id_series is not None:
        ids = pd.Series(id_series).reset_index(drop=True)
    elif id_col in test_df.columns:
        ids = test_df[id_col].reset_index(drop=True)
    elif getattr(test_df.index, "name", None) == id_col:
        ids = test_df.index.to_series().reset_index(drop=True)
    else:
        raise KeyError(f"{id_col} not found. Pass id_series=raw_test['{id_col}'] or keep it in test_df.")

    sub = pd.DataFrame({id_col: ids, "Survived": preds})
    sub.to_csv(out_path, index=False)
    return sub