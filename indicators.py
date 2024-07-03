import pandas as pd

def init_indicators(data):
    ind.add_mvg(data, window_length)
    ind.add_ema(data, window_length)

def add_mvg(data, window_length):
    """
    Adds a regular Moving Average column to the indicators DataFrame.
    """
    name = f'MVG_{window_length}'
    data[name] = data['Close'].rolling(window=window_length, center=False).mean()

    slope_name = f'Slope_MVG_{window_length}'
    data[slope_name] = (data[name] - data[name].shift(1)) 

def add_ema(data, window_length):
    """
    Adds an Exponential Moving Average (EMA) column to the indicators DataFrame.
    """
    name = f'EMA_{window_length}'
    data[name] = data['Close'].ewm(span=window_length, adjust=False).mean()

    slope_name = f'Slope_EMA_{window_length}'
    data[slope_name] = (data[name] - data[name].shift(1)) 
    
def add_rsi(data, window_length):
    """
     Adds an Relative Strength Index (RSI) for a given dataset and window length.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0))
    loss = (-delta.where(delta < 0, 0))
    
    avg_gain = gain.rolling(window=window_length, min_periods=1).mean()
    avg_loss = loss.rolling(window=window_length, min_periods=1).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    data['RSI'] = rsi