import data_readers
import numpy as np

def calculate_stock_performance(data, p=0.02, q=0.01):
    successes = 0
    trials = 0
    window_length = 0 
    
    for idx in range(len(data) - 1):  # Subtract 1 because we need at least one price after idx
        current_price = data['Close'].iloc[idx]
        up_target = current_price * (1+p)
        down_target = current_price * (1-q)
        
        # Look at prices after the current index
        for future_idx, future_price in enumerate(data['Close'].iloc[idx+1:]):
            if future_price >= up_target:
                successes += 1
                window_length = (window_length*idx+future_idx+1)/(idx+1)
                break
            elif future_price <= down_target:
                window_length = (window_length*idx+future_idx+1)/(idx+1)
                break
        
        trials += 1
    
    if trials > 0:
        return successes / trials, window_length
    else:
        return 0, window_length


def test_stock(stock_name, start_date, end_date, p, q):
    """
    Testing the probability 
    """
    data = data_readers.fetch_data(stock_name, start_date, end_date)
    prob, window_length = calculate_stock_performance(data, p, q)

    return prob, window_length, len(data)

def test_sp500(start_date, end_date, p, q):
    
    tickers = data_readers.fetch_sp500_tickers()
    count_profits = 0
    window_lengths = []
    probabilities = []
    profits = []

    for i, ticker in enumerate(tickers):
        prob, window_length, data_length = test_stock(ticker, start_date, end_date, p, q)
        window_lengths += [window_length]
        probabilities += [prob]
        profit = prob * (1+p) + (1-prob) * (1-q)
        profits += [profit]
        count_profits += 1
        print (ticker)
        print ('Prob: ' + str(prob))
        print ('Profit: ' + str(profit))
        print ('Avg length: ' + str(np.average(window_lengths)) + '||' + str(data_length))
        print ('Avg prob: ' + str(np.average(probabilities)))
        print ('Avg profit: ' + str(np.average(profits)))
        
    
test_sp500('2019-01-01', '2024-01-01', p=0.03, q=0.01)
