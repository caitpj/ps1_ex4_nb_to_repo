# Project Title: PS1 Exercise 4 Notebook to Repository

## Overview
This project aims to refactor a Jupyter Notebook into a well-structured Python package. The notebook contains data analysis and visualizations, which will be modularized into separate Python modules for better organization and reusability.

## Directory Structure
The project is organized into the following directories:
- `notebooks/`: Contains the Jupyter Notebook for analysis and visualizations.
- `src/`: Contains the source code organized into modules for data handling, preprocessing, analysis, visualization, and utility functions.
- `tests/`: Contains unit tests for the functions defined in the source code modules.

## Installation
To set up the project environment, you can use the `environment.yml` file. This file lists all the required dependencies for the project.

1. Create a new conda environment:
   ```
   conda env create -f environment.yml
   ```

2. Activate the environment:
   ```
   conda activate <environment_name>
   ```

## Usage
After setting up the environment, you can run the Jupyter Notebook located in the `notebooks/` directory to perform the analysis. The notebook will import functions from the modules in the `src/` directory.

## Contributing
Contributions are welcome! Please create a new branch for any feature or bug fix and submit a pull request for review.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.