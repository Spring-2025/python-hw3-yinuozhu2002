import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(symbol):
  
    data = yf.download(symbol)
    expected_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    for col in expected_cols:
        if col not in data.columns:
            data[col] = np.nan

    return data

def YahooData2returns(YahooData):
  
    # 1) Extract all columns
    open_prices = YahooData['Open']
    high_prices = YahooData['High']
    low_prices  = YahooData['Low']
    close_prices = YahooData['Close']
    adj_close_prices = YahooData['Adj Close']
    volume_data = YahooData['Volume']

    # 2) Use 'Adj Close' to compute returns
    pricevec = adj_close_prices.values
    returns = (pricevec[1:] / pricevec[:-1]) - 1

    return returns
