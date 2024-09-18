# Beer Sales Regression and Classification

## Overview

This project focuses on analyzing beer sales data to build regression and classification models. The goal is to predict the sales channel (e.g., grocery stores vs. mass retailers) and the spend per trip using various machine learning techniques. The project leverages both R and Python for data processing, visualization, and model building.

## Features

- **Data Cleaning and Preparation**: Load and preprocess beer sales data.
- **Exploratory Data Analysis (EDA)**: Visualize data to understand patterns and relationships.
- **Feature Engineering**: Create new features to improve model performance.
- **Model Building**: Train and evaluate regression and classification models.
- **Model Tuning**: Optimize model hyperparameters for better performance.
- **Visualization**: Generate plots to visualize model performance and data insights.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/beer_sales_regression_and_classification.git
   cd beer_sales_regression_and_classification
   ```
2. **Install dependencies**:

   - For R:
     ```r
     install.packages(c("tidyverse", "DT", "GGally", "ggcorrplot", "MASS", "flexdashboard", "plotly", "crosstalk", "knitr", "tidymodels", "reticulate", "lubridate", "scales", "vip", "rpart", "rpart.plot", "NeuralNetTools"))
     ```
   - For Python:
     ```sh
     pip install pandas
     ```
3. **Set up Python environment**:

   - Ensure you have Python installed and accessible from R using the `reticulate` package.

## Usage

1. **Load the data**:

   - Place the `BeerPurchases.csv` file in the project directory.
2. **Run the analysis**:

   - Open the `beer_sales_analysis.qmd` file in RStudio or any other Quarto-compatible editor.
   - Execute the code chunks to perform data analysis, model building, and visualization.

## Project Structure

- `beer_sales_analysis.qmd`: Main analysis script containing all the code for data processing, visualization, and model building.
- `BeerPurchases.csv`: Dataset containing beer sales data.
- `requirements.txt`: List of Python dependencies.

## Key Components

- **Data Loading**: Load beer sales data using both R and Python.
- **Data Cleaning**: Remove unnecessary columns, handle missing values, and create new features.
- **Exploratory Data Analysis (EDA)**: Visualize unique counts, total sales by day of the week, and total sales by month.
- **Feature Engineering**: Create binary columns for weekend/weekday, categorize spend per trip, and aggregate data for trips and customers.
- **Model Building**: Train decision tree, support vector classifier, Lasso regression, and neural network models.
- **Model Evaluation**: Evaluate model performance using metrics like accuracy, sensitivity, specificity, precision, RMSE, MAE, and R-squared.
- **Visualization**: Generate plots for unique counts, total sales, ROC curves, and model importance.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact: soltauryan@gmail.com
