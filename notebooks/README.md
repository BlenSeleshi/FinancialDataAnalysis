**\*\*\*\***\***\*\*\*\*** Task 1: SENTIMENT ANALYSIS (sentimentAnalysis.ipynb)\***\*\*\*\*\***\*\*\*\***\*\*\*\*\***

## Sentiment Analysis of Analyst Ratings - Jupyter Notebook

This Jupyter Notebook explores the sentiment of analyst ratings headlines.

**Functionality:**

- Loads and analyzes a dataset of analyst ratings (CSV format)
- Performs basic exploratory data analysis
- Analyzes headline length distribution
- Explores publication date trends over time (including seasonality)
- Conducts sentiment analysis of headlines
- Identifies publishers with the most positive/negative/neutral articles
- Analyzes sentiment distribution across top publishers
- Extracts domains from publisher names and analyzes domain distribution
- Identifies top stocks with highest positive/negative/neutral scores
- Performs basic topic modelling using word clouds
- Analyzes sentiment for specific stocks (AAPL, AMZN, GOOG, NVDA)

**Instructions:**

1. Replace `r'C:\Users\Blen\OneDrive\Documents\10Academy\Week1\Data\raw_analyst_ratings.csv'` with the actual path to your CSV file in the first code cell.
2. Run each code cell individually to perform the analysis.

**Dependencies:**

- pandas: Used for loading, cleaning, and transforming the dataset.
- numpy: Provides support for numerical operations, arrays, and matrices.
- matplotlib.pyplot: Used for creating various plots like histograms, bar charts, and time series visualizations
- seaborn: Offers a more concise and aesthetically pleasing interface for creating statistical graphics.
- nltk: Used for sentiment analysis using the Vader sentiment analyzer.
- sklearn: Used for feature extraction (CountVectorizer) in topic modeling.
- wordcloud: Used to visualize the most common words in the headlines.
- statsmodels: Used for time series analysis and decomposition.

**Please note:** This code utilizes pre-existing libraries. Ensure you have them installed before running the notebook.

### For the technical_analysis

````markdown
# TASK -2 Technical Analysis Notebook

This Jupyter Notebook demonstrates how to perform technical stock analysis using Python. It includes steps for loading data, applying technical indicators, and visualizing the results.

## Features

1. **Data Loading**
   - Load stock data from a CSV file.
2. **Technical Indicators**

   - Calculate and visualize the Simple Moving Average (SMA), Exponential Moving Average (EMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD).

3. **Data Cleaning**

   - Remove unnecessary columns from the DataFrame for a more focused analysis.

4. **Visualization**
   - Generate plots for the Close Price, SMA, EMA, RSI, and MACD.

## Usage

To use this notebook, run the cells in order. Ensure that you update the file path to your stock data CSV in the `load_data` function call.

## Dependencies

- pandas
- matplotlib
- numpy
- Jupyter Notebook

## Running the Notebook

1. Clone the repository or download the notebook.
2. Install the required dependencies.
3. Run the notebook in Jupyter.

Certainly! Here’s a sample README file content for your project that explains the purpose of the code, how it works, and how to use it:

---

# TASK -3 Sentiment and Stock Correlation Analysis

## Overview

This project analyzes the relationship between sentiment scores derived from news headlines and daily stock returns for four major tech companies: Apple Inc. (AAPL), Amazon.com Inc. (AMZN), Alphabet Inc. (GOOG), and NVIDIA Corporation (NVDA). The analysis includes sentiment score calculation, daily return computation, and correlation between sentiment and stock performance.

## Files and Structure

- `raw_analyst_ratings.csv`: Contains sentiment data with headlines and associated dates.
- `yfinance_data/AAPL_historical_data.csv`: Historical stock data for Apple Inc.
- `yfinance_data/AMZN_historical_data.csv`: Historical stock data for Amazon.com Inc.
- `yfinance_data/GOOG_historical_data.csv`: Historical stock data for Alphabet Inc.
- `yfinance_data/NVDA_historical_data.csv`: Historical stock data for NVIDIA Corporation.

## Dependencies

The code requires the following Python packages:

- `pandas`
- `textblob`
- `datetime`

Install the required packages using pip:

```bash
pip install pandas textblob
```

## Code Description

### 1. Importing the Necessary Packages

```python
import pandas as pd
from datetime import datetime
import textblob
```

### 2. Normalize Dates and Filter Stocks

- Load the sentiment data.
- Drop the URL column.
- Convert the 'date' column to a datetime format.
- Filter the data to include only the relevant stocks.

### 3. Calculate Sentiment Scores

- Define a function to calculate sentiment scores using TextBlob.
- Apply sentiment analysis to the headlines.
- Aggregate sentiment scores by date and stock.

### 4. Process Stock Data

- Load historical stock data for each relevant stock.
- Convert the 'Date' column to datetime format.
- Drop unnecessary columns such as Dividends, Stock Splits, and Volume.
- Calculate daily returns for each stock.

### 5. Merge Data for Correlation Analysis

- Merge the sentiment data with the stock data based on the date.
- Keep necessary columns for analysis.

### 6. Calculate Correlation

- Compute Pearson correlation between sentiment scores and daily returns for each stock.
- Print the correlation results.

## Usage

1. Ensure all required packages are installed.
2. Place the CSV files in the specified directories.
3. Run the notebboks to perform the analysis.

## Results

The script outputs the Pearson correlation coefficient between sentiment scores and daily stock returns for each of the four stocks. This helps in understanding how news sentiment affects stock performance.

## Notes

- The sentiment score is derived from the headline text using TextBlob.
- Daily returns are calculated as the percentage change from the opening price to the closing price.
- Correlations are computed to identify potential relationships between sentiment and stock performance.

```bash
pip install pandas matplotlib numpy
```
````
