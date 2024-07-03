import indicators as ind
import trading_strategies as strg
import data_readers

def backtest(stock_name, start_date, end_date, window_length):
    data = data_readers.fetch_data(stock_name, start_date, end_date)
    ind.add_mvg(data, window_length)
    ind.add_ema(data, window_length)

    capital = 1.0
    current_position = False
    purchased_price = None
    sales = []
    purchases = []

    for idx in range(len(data)):
        previous_position = current_position
        current_position = strg.strategy(data, current_position, 
                                        idx, strg.avg_holding, strg.avg_stop_loss, 
                                        window_length)
        
        if current_position == False and previous_position == True:
            # if we sold the ticket -->
            capital = capital * (data['Close'].iloc[idx]/purchased_price)
            purchases += [False]
            sales += [True]
        elif current_position == True and idx == len(data) - 1: 
            # we sell at the end -->
            capital = capital * (data['Close'].iloc[idx]/purchased_price)
            purchases += [False]
            sales += [True]
        elif current_position == True and previous_position == False: 
            # if we bought -->
            purchased_price = data['Close'].iloc[idx]
            purchases += [True]
            sales += [False]
        else:
            purchases += [False]
            sales += [False]
    
    data['Purchases'] = purchases
    data['Sales'] = sales

    return data, capital


def back_test_sp500():
    
    tickers = data_readers.fetch_sp500_tickers()
    avg_return = 0

    for i, ticker in enumerate(tickers):
        _, total_returns = backtest(ticker, start_date = '2020-01-01', end_date = '2024-01-01', window_length=100)
        avg_return = (avg_return*i + total_returns)/(i+1)
        print (ticker + ' returns: ' + str(total_returns))
        print ('Average return: ' + str(avg_return))

total_returns = backtest('NVDA', start_date = '2020-01-01', end_date = '2024-01-01', window_length=100)
print ('NVDA' + ' returns: ' + str(total_returns))
#back_test_sp500()


    