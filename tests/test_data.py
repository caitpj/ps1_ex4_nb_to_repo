import pytest
from src.ps1_ex4_nb_to_repo.data import load_data, save_data

def test_load_data():
    # Test loading data from a valid file
    data = load_data('path/to/valid/file.csv')
    assert data is not None
    assert isinstance(data, pd.DataFrame)

def test_load_data_invalid_file():
    # Test loading data from an invalid file
    with pytest.raises(FileNotFoundError):
        load_data('path/to/invalid/file.csv')

def test_save_data(tmp_path):
    # Test saving data to a file
    data = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
    save_data(data, tmp_path / 'test_file.csv')
    
    # Verify the file was created
    assert (tmp_path / 'test_file.csv').is_file() 

    # Verify the contents of the saved file
    loaded_data = load_data(tmp_path / 'test_file.csv')
    pd.testing.assert_frame_equal(data, loaded_data)