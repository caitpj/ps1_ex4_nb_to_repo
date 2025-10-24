import pytest
from ps1_ex4_nb_to_repo.analysis import perform_analysis, summarize_results

def test_perform_analysis():
    # Example input data
    input_data = [1, 2, 3, 4, 5]
    expected_output = 3  # Replace with the expected output of the analysis function

    # Call the function
    result = perform_analysis(input_data)

    # Assert the result is as expected
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_summarize_results():
    # Example results data
    results = {'mean': 3, 'median': 3, 'std_dev': 1.58}  # Replace with actual expected summary

    # Call the function
    summary = summarize_results(results)

    # Assert the summary is as expected
    assert summary['mean'] == results['mean'], "Mean does not match"
    assert summary['median'] == results['median'], "Median does not match"
    assert summary['std_dev'] == results['std_dev'], "Standard deviation does not match"