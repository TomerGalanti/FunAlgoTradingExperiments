import math 

##### momentum v1 #####
def momentum_strategy(data, previous_position, idx, stop_loss_percent=0.0, max_gap=0.8, max_slope=0.01, window_length=150):
    """
    The strategy micha.stocks promoted
    """

    name = f'MVG_{window_length}'
    slope_name = f'Slope_MVG_{window_length}'

    current_price = data['Close'].iloc[idx]
    current_avg = data[name].iloc[idx]
    current_slope = data[slope_name].iloc[idx]/current_price
    price_gap = (current_price - current_avg)/current_price

    # Check for sufficient data
    if idx < window_length:
        return False  # Not enough data

    if previous_position == True and current_price < current_avg * (1-stop_loss_percent):
        # if the price dropped below the moving average --> sell
        return False

    if previous_position == False and current_slope > 0 and current_slope < max_slope and price_gap > 0 and price_gap < max_gap:
        # if there is a momentum --> buy
        return True
    else:
        # otherwise, keep the same position
        return previous_position


##### momentum v2 #####
def momentum_strategy_enhanced(data, previous_position, idx, 
                            stop_loss_percent=0.0, max_gap=1, max_slope=0.01,
                            window_length=150, volume_factor=.5, rsi_threshold=70):
    """
    Enhanced momentum strategy with dynamic features and additional indicators.
    """
    name = f'MVG_{window_length}'
    slope_name = f'Slope_MVG_{window_length}'

    current_price = data['Close'].iloc[idx]
    current_avg = data[name].iloc[idx]
    current_slope = data[slope_name].iloc[idx] / current_price
    price_gap = (current_price - current_avg) / current_price
    current_volume = data['Volume'].iloc[idx]
    avg_volume = data['Volume'].rolling(window=window_length).mean().iloc[idx]
    current_rsi = data['RSI'].iloc[idx]

    # Check for sufficient data
    if idx < window_length:
        return False  # Not enough data

    if previous_position == True:
        if current_price < current_avg * (1 - stop_loss_percent):
            return False  # Stop loss
        if current_rsi > rsi_threshold:
            return False  # Overbought, time to sell

    if previous_position == False:
        if (current_slope > 0 and current_slope < max_slope and 
            price_gap > 0 and price_gap < max_gap and 
            current_volume > volume_factor * avg_volume and 
            current_rsi < rsi_threshold):
            return True  # Conditions met for a strong buy signal
    return previous_position


