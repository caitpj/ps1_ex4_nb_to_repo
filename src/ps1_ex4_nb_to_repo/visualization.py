def plot_data(data, x_column, y_column, title='Data Plot', xlabel='X-axis', ylabel='Y-axis'):
    """
    Plots the given data using the specified x and y columns.

    Parameters:
    - data: DataFrame containing the data to plot.
    - x_column: The column name to be used for the x-axis.
    - y_column: The column name to be used for the y-axis.
    - title: Title of the plot (default is 'Data Plot').
    - xlabel: Label for the x-axis (default is 'X-axis').
    - ylabel: Label for the y-axis (default is 'Y-axis').

    Returns:
    - None: Displays the plot.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(data[x_column], data[y_column], marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()


def show_results(results):
    """
    Displays the results of the analysis in a readable format.

    Parameters:
    - results: The results to display, typically a DataFrame or summary statistics.

    Returns:
    - None: Prints the results to the console.
    """
    print("Analysis Results:")
    print(results)