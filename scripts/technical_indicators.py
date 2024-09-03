# technical_indicators.py

import pandas as pd
import numpy as np

def load_data(file_path):
    
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    return df

def calculate_sma(df, window):
# Calculate the simple moving average
    return df['Close'].rolling(window=window).mean()

def calculate_ema(df, window):
    
   # Calculate the Exponential Moving Average (EMA).
    
    return df['Close'].ewm(span=window, adjust=False).mean()

def calculate_rsi(df, window=14):
    
    # Calculate the Relative Strength Index (RSI).
    
   
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    
  #  Calculate the Moving Average Convergence Divergence (MACD).
    
    ema_short = df['Close'].ewm(span=short_window, adjust=False).mean()
    ema_long = df['Close'].ewm(span=long_window, adjust=False).mean()
    
    macd = ema_short - ema_long
    macd_signal = macd.ewm(span=signal_window, adjust=False).mean()
    
    return macd, macd_signal

def apply_technical_indicators(df):
    
   # Apply all technical indicators to the DataFrame.
    
    df['SMA_20'] = calculate_sma(df, window=20)
    df['EMA_20'] = calculate_ema(df, window=20)
    df['RSI'] = calculate_rsi(df, window=14)
    df['MACD'], df['MACD_Signal'] = calculate_macd(df, short_window=12, long_window=26, signal_window=9)
    return df

def clean_data(df):

   # Remove irrelevant columns from the DataFrame.
   
    relevant_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20', 'EMA_20', 'RSI', 'MACD', 'MACD_Signal']
    return df[relevant_columns]
