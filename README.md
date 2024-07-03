# Stock Backtesting Framework

This project provides a generic framework for backtesting trading strategies on historical stock data. It includes functions to fetch data, apply indicators, and execute strategies on both individual stocks and the S&P 500 index.

## Installation

Ensure you have the necessary dependencies installed. You can use `pip` to install them:

```sh
pip install pandas numpy, pandas, yfinance, matplotlib

```

## Usage

Backtesting a Single Stock
The backtest function performs a backtest on a single stock using a specified trading strategy. It calculates the performance of the strategy over a given time period.

Parameters

stock_name: The ticker symbol of the stock to backtest. \
start_date: The start date of the backtest period in YYYY-MM-DD format. \
end_date: The end date of the backtest period in YYYY-MM-DD format. \
strategy_fn: The trading strategy function to use. \

Example: backtest_sp500('2019-01-01', '2024-01-01', moving_average_strategy)

## Indicators

The framework includes several technical indicators that can be added to the stock data:

Exponential Moving Average (EMA)
Simple Moving Average (SMA)
Relative Strength Index (RSI)
These indicators are added to the data using the indicators module.

Strategies

The framework allows you to define custom trading strategies. A strategy function takes the stock data, the current position, and the current index as inputs, and returns whether to be in a position or not.

Example strategy functions are included in the strategies module.
