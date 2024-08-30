**\*\*\*\***\***\*\*\*\*** Task 1: SENTIMENT ANALYSIS (sentimentAnalysis.ipynb)****\*\*****\*\*\*****\*\*****

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
