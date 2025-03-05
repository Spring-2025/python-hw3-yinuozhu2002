import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(symbol, start=None, end=None):
  
    data = yf.download(symbol, start=start, end=end)
    return data

def YahooData2returns(YahooData):
   
    prices = YahooData['Adj Close']
    pricevec = prices.values
    returns = (pricevec[1:] / pricevec[:-1]) - 1
    return returns

