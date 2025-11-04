import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def combine_train_test(train_df: pd.DataFrame, test_df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine train and test DataFrames for exploratory analysis.
    Adds a 'set' column to differentiate them.

    Returns
    -------
    pd.DataFrame
        Combined DataFrame with 'set' = 'train' or 'test'.
    """
    all_df = pd.concat([train_df, test_df], axis=0)
    all_df["set"] = "train"
    all_df.loc[all_df["Survived"].isna(), "set"] = "test"
    return all_df

def plot_univariate_categorical(all_df: pd.DataFrame, cols: list[str]):
    """
    Plot count distributions for categorical variables comparing train/test.
    """
    for col in cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(x=col, data=all_df, hue="set", palette="Set2")
        plt.title(f"Distribution of {col} in train/test sets")
        plt.grid(color="black", linestyle="--", linewidth=0.5, axis="y")
        plt.show()

def plot_univariate_by_survival(train_df: pd.DataFrame, cols: list[str]):
    """
    Plot categorical distributions split by 'Survived' for training data.
    """
    for col in cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(x=col, data=train_df, hue="Survived", palette="coolwarm")
        plt.title(f"{col} distribution by Survival")
        plt.grid(color="black", linestyle="--", linewidth=0.5, axis="y")
        plt.show()

def plot_numeric_distributions(train_df: pd.DataFrame, features: list[str]):
    """
    Plot histograms of numerical features split by 'Survived'.
    """
    for feature in features:
        plt.figure(figsize=(8, 4))
        sns.histplot(data=train_df, x=feature, hue="Survived", kde=True, palette="coolwarm", bins=30)
        plt.title(f"Distribution of {feature} by Survival")
        plt.grid(color="black", linestyle="--", linewidth=0.5, axis="y")
        plt.show()

def add_family_size(df):
    """
    Add a 'Family Size' feature based on SibSp (siblings/spouses)
    and Parch (parents/children).

    Formula:
        Family Size = SibSp + Parch + 1

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing 'SibSp' and 'Parch'.

    Returns
    -------
    pd.DataFrame
        DataFrame with an added 'Family Size' column.
    """
    df["Family Size"] = df["SibSp"] + df["Parch"] + 1
    return df

def add_age_interval(df):
    """
    Add an 'Age Interval' categorical feature by binning ages.
    """
    bins   = [-1, 16, 32, 48, 64, float("inf")]
    labels = [0, 1, 2, 3, 4]
    df["Age Interval"] = pd.cut(df["Age"], bins=bins, labels=labels)
    df["Age Interval"] = df["Age Interval"].astype("Int64")  # <- allow NA
    return df

def add_fare_interval(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'Fare Interval' categorical feature by binning fares.

    Bins:
        0: <= 7.91
        1: 7.91–14.454
        2: 14.454–31
        3: > 31
    """
    bins = [-1, 7.91, 14.454, 31, float("inf")]
    labels = [0, 1, 2, 3]
    df["Fare Interval"] = pd.cut(df["Fare"], bins=bins, labels=labels)

    # Convert safely to integer, keeping NaNs untouched
    df["Fare Interval"] = df["Fare Interval"].astype("Int64")

    return df

def add_sex_pclass(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a composed categorical feature combining Sex and Pclass.
    Example output: 'F_C1', 'M_C3'
    """
    df["Sex_Pclass"] = df.apply(lambda row: str(row["Sex"])[0].upper() + "_C" + str(row["Pclass"]), axis=1)
    return df

def plot_count_grouped(df, x_col: str, group_by: str):
    """
    Count plot of x_col, grouped by group_by (single hue).
    Casts to string so nullable ints / categories plot cleanly.
    """
    data = df.copy()
    data[x_col] = data[x_col].astype("string")
    data[group_by] = data[group_by].astype("string")

    plt.figure(figsize=(8, 4))
    sns.countplot(x=x_col, hue=group_by, data=data, dodge=True)
    plt.title(f"{x_col} grouped by {group_by}")
    plt.grid(color="black", linestyle="--", linewidth=0.5, axis="y")
    plt.show()

def add_family_type(df):
    """
    Add a categorical 'Family Type' feature based on 'Family Size'.

    Categories:
        - Single : 1 member
        - Small  : 2–4 members
        - Large  : 5 or more
    """
    df["Family Type"] = "Unknown"  # default
    df.loc[df["Family Size"] == 1, "Family Type"] = "Single"
    df.loc[(df["Family Size"] > 1) & (df["Family Size"] < 5), "Family Type"] = "Small"
    df.loc[df["Family Size"] >= 5, "Family Type"] = "Large"
    return df