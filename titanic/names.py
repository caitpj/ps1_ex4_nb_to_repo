import pandas as pd

def parse_name(row: pd.Series) -> pd.Series:
    """
    Extract structured name information from the Titanic 'Name' field.

    Returns:
        pd.Series with:
            - Family Name
            - Title
            - Given Name
            - Maiden Name (if present)
    """
    try:
        text = row["Name"]
        split_text = text.split(",")
        family_name = split_text[0].strip()
        next_text = split_text[1].strip()

        # Extract title (e.g., Mr., Mrs., Miss.)
        parts = next_text.split(".")
        title = parts[0].strip() + "."
        next_text = parts[1].strip() if len(parts) > 1 else ""

        # Extract given and maiden names if parentheses present
        if "(" in next_text:
            given, maiden = next_text.split("(", 1)
            given_name = given.strip()
            maiden_name = maiden.rstrip(")").strip()
        else:
            given_name, maiden_name = next_text, None

        return pd.Series([family_name, title, given_name, maiden_name])
    except Exception as ex:
        print(f"Exception: {ex}")
        return pd.Series([None, None, None, None])


def apply_name_parsing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply parse_name() across a Titanic dataset to extract name components.
    """
    df[["Family Name", "Title", "Given Name", "Maiden Name"]] = df.apply(parse_name, axis=1)
    return df

