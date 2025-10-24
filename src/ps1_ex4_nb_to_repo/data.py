def load_data(file_path):
    """
    Load data from a specified file path.

    Parameters:
    file_path (str): The path to the data file.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    import pandas as pd
    return pd.read_csv(file_path)


def save_data(data, file_path):
    """
    Save data to a specified file path.

    Parameters:
    data (DataFrame): The pandas DataFrame to save.
    file_path (str): The path where the data will be saved.
    """
    data.to_csv(file_path, index=False)