import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(YahooData):
    prices = YahooData['Adj Close']
    returns = prices.pct_change().dropna()
    return returns.values

def get_stock_data(symbol):
    data = yf.download(symbol)
    prices = data['Adj Close']
    return prices
