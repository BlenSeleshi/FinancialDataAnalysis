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
# Technical Analysis Notebook

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

```bash
pip install pandas matplotlib numpy jupyter
```
````
