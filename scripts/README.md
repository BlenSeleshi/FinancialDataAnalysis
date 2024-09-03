# Technical Indicators Script

This script provides functions for loading financial stock data, applying technical indicators, and cleaning the data for analysis.

## Functions

1. **load_data(file_path)**

   - **Description**: Loads stock data from a CSV file and parses dates.
   - **Parameters**:
     - `file_path`: The path to the CSV file containing the stock data.
   - **Returns**: A pandas DataFrame containing the loaded data.

2. **apply_technical_indicators(df)**

   - **Description**: Calculates and applies technical indicators such as SMA, EMA, RSI, and MACD to the DataFrame.
   - **Parameters**:
     - `df`: A pandas DataFrame containing the stock data.
   - **Returns**: A DataFrame with the technical indicators added as new columns.

3. **clean_data(df)**
   - **Description**: Removes irrelevant columns from the DataFrame, keeping only the necessary columns for analysis.
   - **Parameters**:
     - `df`: A pandas DataFrame containing the stock data with technical indicators.
   - **Returns**: A cleaned DataFrame with only relevant columns.

## Usage

```python
from scripts.technical_indicators import load_data, apply_technical_indicators, clean_data

# Load the stock data
df = load_data('your_data.csv')

# Apply technical indicators
df = apply_technical_indicators(df)

# Clean the data
df = clean_data(df)
```
