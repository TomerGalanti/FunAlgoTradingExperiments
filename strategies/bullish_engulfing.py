
##### Bullish engulfing ######
def bullish_engulfing_strategy(data, previous_position, idx):
    """
    Predicting bullish behavior based on a bullish engulfing candle
    """

    if idx == 0 or idx == 1:
        return False  # There is no previous candle at index 0

    if previous_position == True:
        return False

    # Current and previous candle data
    curr_open = data['Open'].iloc[idx]
    curr_close = data['Close'].iloc[idx]
    prev_open = data['Open'].iloc[idx-1]
    prev_close = data['Close'].iloc[idx-1]

    # Check if the current candle is green and the previous one is red
    is_curr_green = curr_close > curr_open
    is_prev_red = prev_close < prev_open

    # Check if the current green candle fully engulfs the previous red candle
    is_engulfing = is_curr_green and is_prev_red and \
                   (curr_open < prev_close and curr_close > prev_open)

    return is_engulfing


def calculate_fibonacci_levels(high, low):
    """
    Calculate Fibonacci retracement levels.
    """
    difference = high - low
    first = high - difference * 0.236
    second = high - difference * 0.382
    third = high - difference * 0.5
    fourth = high - difference * 0.618
    fifth = high - difference * 0.764
    return [first, second, third, fourth, fifth]


def be_with_fib_strategy(data, previous_position, idx, lookback_period=20):
    """
    Predicting bullish behavior based on a bullish engulfing candle and
    using Fibonacci retracement for confirmation.
    """
    if idx == 0 or idx < lookback_period:
        return False  # Not enough data to calculate Fibonacci levels

    if previous_position == True:
        return False

    # Current and previous candle data
    curr_open = data['Open'].iloc[idx]
    curr_close = data['Close'].iloc[idx]
    prev_open = data['Open'].iloc[idx-1]
    prev_close = data['Close'].iloc[idx-1]

    # Check for bullish engulfing
    is_curr_green = curr_close > curr_open
    is_prev_red = prev_close < prev_open
    is_engulfing = is_curr_green and is_prev_red and (curr_open < prev_close and curr_close > prev_open)

    if not is_engulfing:
        return False

    # Calculate Fibonacci retracement levels from the last lookback_period
    recent_high = data['High'][idx-lookback_period:idx].max()
    recent_low = data['Low'][idx-lookback_period:idx].min()
    fibonacci_levels = calculate_fibonacci_levels(recent_high, recent_low)

    # Example use-case: Check if current close is near any Fibonacci level (for simplicity, within 0.5% of a level)
    for level in fibonacci_levels:
        if abs(curr_close - level) / level < 0.005:
            return True

    return False

