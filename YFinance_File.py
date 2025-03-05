import yfinance as yf
import pandas as pd
import numpy as np


def YahooData2returns(YahooData):
    prices = YahooData['Adj Close']
    returns = prices.pct_change().dropna()

    return returns

def get_stock_data(symbol):
    data = yf.download(symbol)
    prices = data['Adj Close']
    return prices


prices = get_stock_data('GS')
print(type(prices))
pricevec = prices.values

def get_returns(pricevec):
    n = len(pricevec)
    ratiovec = pricevec[1:n] / pricevec[0:n - 1]
    returns = ratiovec - 1
    return returns

returns = get_returns(pricevec)
print(returns)