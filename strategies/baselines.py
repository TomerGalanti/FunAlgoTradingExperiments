
##### Buy and hold strategy #####
def buy_and_hold_strategy(data, previous_position, idx):
    if idx != len(data)-1:
        return True # Keep the stock
    else:
        return False # Sell the stock

def moving_average_strategy(data, previous_position, idx):
    # Check if sufficient data exists to make a decision
    if idx < 50:
        return False # Not enough data to make a decision, so default to False (sell)

    # Decision logic based on moving averages at the given index
    if data['MVG_10'].iloc[idx] < data['MVG_50'].iloc[idx]:
        return True # True to hold the stock
    else:
        return False # False to sell the stock

def dynamics_threshold_crossover_strategy(data, previous_position, idx, rsi_period=14, overbought=100):

    # Check if there's enough data to compute indicators
    if idx < 50:
        return False  # Not enough data to make a decision

    # Calculate moving averages at index
    short_ma = data['MVG_10'].iloc[idx]
    long_ma = data['MVG_50'].iloc[idx]
    rsi = data['RSI'].iloc[idx]

    # Decision logic based on indicators at the specific index
    if short_ma > long_ma and rsi < overbought:
        return True  # True to hold the stock
    else:
        return False  # False to sell the stock