import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


def fetch_data(stock_symbol, start_date, end_date):
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data

def fetch_sp500_tickers():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    sp500 = table[0]
    tickers = sp500['Symbol'].tolist()
    return tickers