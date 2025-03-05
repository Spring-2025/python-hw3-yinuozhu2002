import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(YahooData):
    prices = YahooData['Adj Close']
    returns = prices.pct_change().dropna()
    return returns
