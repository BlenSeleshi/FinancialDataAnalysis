# Stock Sentiment Analysis and Technical Indicators

## Overview

This project analyzes over 1 million news articles about various stocks and examines their sentiment over time. It also includes technical analysis of stock data using indicators like SMA, EMA, RSI, and MACD. The project is divided into three main notebooks:

1. **Sentiment Analysis**: Analyzes sentiment from news headlines and visualizes trends, publisher statistics, and sentiment distribution across different stocks.
2. **Technical Analysis**: Applies technical indicators to stock data and visualizes the results.
3. **Correlation Analysis**: Correlates sentiment scores with stock price movements to explore potential relationships.

## Project Structure

- `notebooks/`
  - `Sentiment_Analysis.ipynb`: Performs sentiment analysis on news headlines, including visualization and publisher analysis.
  - `Technical_Analysis.ipynb`: Analyzes stock data using technical indicators.
  - `Correlation_Analysis.ipynb`: Correlates sentiment scores with stock price movements.
- `scripts/`
  - `technical_indicators.py`: Contains functions for calculating technical indicators like SMA, EMA, RSI, and MACD.
- `data/`
  - `raw_analyst_ratings.csv`: Dataset with news headlines and metadata.
  - `yfinance_data/`: Directory containing historical stock data for various companies.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   Make sure to create a `requirements.txt` file with the necessary dependencies. For example:

   ```
   pandas
   numpy
   matplotlib
   seaborn
   nltk
   scikit-learn
   wordcloud
   statsmodels
   textblob
   ```

## Usage

1. **Sentiment Analysis:**

   Open `Sentiment_Analysis.ipynb` in Jupyter Notebook or JupyterLab and run the cells to perform sentiment analysis on the headlines.

2. **Technical Analysis:**

   Open `Technical_Analysis.ipynb` and execute the cells to apply technical indicators to stock data.

3. **Correlation Analysis:**

   Open `Correlation_Analysis.ipynb` to correlate sentiment scores with stock price movements.

## Data

- `raw_analyst_ratings.csv`: Contains news headlines and related metadata.
- `yfinance_data/`: Contains historical stock price data for various companies.

## Notes

- Ensure that paths to datasets in the notebooks and scripts are correctly set according to your local environment.
- If you encounter any issues or have questions, please open an issue on the GitHub repository.
