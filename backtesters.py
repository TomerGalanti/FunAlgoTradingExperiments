import indicators as ind
from strategies import *
import data_readers

def backtest(stock_name, start_date, end_date, strategy_fn):
    """
    Generic backtest function
    """
    data = data_readers.fetch_data(stock_name, start_date, end_date)
    
    ind.add_ema(data, 150)

    ind.add_mvg(data, 150)
    ind.add_mvg(data, 50)
    ind.add_mvg(data, 10)

    ind.add_rsi(data, 14)

    capital = 1.0
    current_position = False
    purchased_price = None
    sales = []
    purchases = []

    for idx in range(len(data)):
        previous_position = current_position
        current_position = strategy_fn(data, current_position, idx)
        
        if current_position == False and previous_position == True:
            # if we sell the ticket -->
            capital = capital * (data['Close'].iloc[idx]/purchased_price)
            purchases += [False]
            sales += [True]
        elif current_position == True and idx == len(data) - 1: 
            # we sell at the end -->
            capital = capital * (data['Close'].iloc[idx]/purchased_price)
            purchases += [False]
            sales += [True]
        elif current_position == True and previous_position == False: 
            # if we buy -->
            purchased_price = data['Close'].iloc[idx]
            purchases += [True]
            sales += [False]
        else:
            purchases += [False]
            sales += [False]
    
    data['Purchases'] = purchases
    data['Sales'] = sales

    return data, capital


def backtest_sp500(start_date, end_date, strategy_fn):
    
    tickers = data_readers.fetch_sp500_tickers()
    avg_return = 0

    for i, ticker in enumerate(tickers):
        _, total_returns = backtest(ticker, start_date, end_date, strategy_fn)
        avg_return = (avg_return*i + total_returns)/(i+1)
        print (ticker + ' returns: ' + str(total_returns))
        print ('Average return: ' + str(avg_return))

        _, total_returns = backtest(ticker, start_date, end_date, buy_and_hold_strategy)
        print (ticker + ' returns: ' + str(total_returns))


backtest_sp500('2019-01-01', '2024-01-01', moving_average_strategy)


    