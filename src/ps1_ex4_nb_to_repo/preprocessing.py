def clean_data(data):
    """
    Cleans the input data by handling missing values and removing duplicates.

    Parameters:
    data (DataFrame): The input data to be cleaned.

    Returns:
    DataFrame: The cleaned data.
    """
    # Remove duplicates
    data = data.drop_duplicates()
    # Fill missing values with the mean of the column
    data = data.fillna(data.mean())
    return data


def transform_data(data):
    """
    Transforms the input data by normalizing numerical features.

    Parameters:
    data (DataFrame): The input data to be transformed.

    Returns:
    DataFrame: The transformed data with normalized features.
    """
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    numerical_cols = data.select_dtypes(include=['float64', 'int']).columns
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    return data