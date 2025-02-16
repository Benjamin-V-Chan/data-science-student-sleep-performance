# data-science-student-sleep-performance

# Sleep Deprivation & Cognitive Performance Analysis

## Project Overview
This project explores the impact of sleep deprivation on cognitive performance using statistical analysis, correlation studies, and machine learning models. The dataset includes sleep hours, cognitive test scores, and other behavioral factors.

## Folder Structure
```
project-root/
├── data/                # Contains raw and cleaned datasets
│   ├── sleep_deprivation_dataset_detailed.csv
│   ├── cleaned_sleep_data.csv
├── scripts/             # Contains Python scripts for analysis
│   ├── 01_load_and_clean.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_correlation_analysis.py
│   ├── 04_regression_model.py
│   ├── 05_visualization.py
├── outputs/             # Stores generated visualizations and reports
│   ├── sleep_hours_distribution.png
│   ├── correlation_matrix.png
│   ├── regression_results.txt
│   ├── sleep_vs_reaction.png
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
```

## Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### 2. Data Cleaning:
Run the data cleaning script to preprocess the dataset.
```sh
python scripts/01_load_and_clean.py
```

### 3. Exploratory Data Analysis:
Generate summary statistics and visualizations.
```sh
python scripts/02_exploratory_analysis.py
```

### 4. Correlation Analysis:
Compute and visualize the correlation matrix.
```sh
python scripts/03_correlation_analysis.py
```

### 5. Regression Modeling:
Train a regression model to predict cognitive performance based on sleep hours.
```sh
python scripts/04_regression_model.py
```

### 6. Visualization:
Generate scatter plots to analyze trends.
```sh
python scripts/05_visualization.py
```

## Requirements
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

To install all dependencies, use:
```sh
pip install -r requirements.txt
```

## Acknowledgments
**Dataset Name:** Sleep Deprivation & Cognitive Performance  
**Dataset Author:** Sacramento Technology  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/sacramentotechnology/sleep-deprivation-and-cognitive-performance)