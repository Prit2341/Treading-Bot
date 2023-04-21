def is_doji(Live_Data1):
     # Candlestick is a list of [open, high, low, close]
    high_price = max(Live_Data1)
    low_price = min(Live_Data1)
    open_price = Live_Data1[0]
    close_price = Live_Data1[-1]
    candlestick = open_price, high_price, low_price, close_price 
    #Over all Body
    body_size = abs(high_price-low_price)
    # Calculate the body size
    doji_body_size = abs(close_price - open_price)
    # Calculate the upper and lower wick sizes
    upper_wick = high_price - max(close_price, open_price)
    lower_wick = min(close_price, open_price) - low_price
    # Check if the body size is small and the wicks are long
    if doji_body_size <= body_size * 10/100 and upper_wick >= body_size * 30/100 and lower_wick >= body_size * 30/100:
        return True
    return False



        