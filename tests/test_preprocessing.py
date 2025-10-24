import pytest
from ps1_ex4_nb_to_repo.preprocessing import clean_data, transform_data

def test_clean_data():
    # Example input for testing
    raw_data = {
        'column1': [1, 2, None, 4],
        'column2': ['a', 'b', 'c', None]
    }
    
    expected_cleaned_data = {
        'column1': [1, 2, 4],
        'column2': ['a', 'b', 'c']
    }
    
    cleaned_data = clean_data(raw_data)
    
    assert cleaned_data == expected_cleaned_data

def test_transform_data():
    # Example input for testing
    cleaned_data = {
        'column1': [1, 2, 4],
        'column2': ['a', 'b', 'c']
    }
    
    expected_transformed_data = {
        'column1': [1, 4, 2],
        'column2': ['c', 'b', 'a']
    }
    
    transformed_data = transform_data(cleaned_data)
    
    assert transformed_data == expected_transformed_data