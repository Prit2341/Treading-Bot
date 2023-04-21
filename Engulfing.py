#Live_Data1 is the First Candle
#Live_Data2 is for the second cadle
def detect_bullish_engulfing(prices):
      # Initialize a list to store the bullish engulfing patterns
  bullish_engulfing_patterns = []
  
  # Loop through the prices and look for bullish engulfing patterns
  for i in range(1, len(prices)):
    # Check if the current day's price is a large white candlestick that completely engulfs the previous day's small black candlestick
    if prices[i]['close'] > prices[i]['open'] and prices[i]['close'] > prices[i-1]['close'] and prices[i]['open'] < prices[i-1]['open']:
      # If the pattern is found, append it to the list
      bullish_engulfing_patterns.append((i-1, i))
      
  # Return the list of bullish engulfing patterns
  return bullish_engulfing_patterns






def detect_bearish_engulfing(prices):
      # Initialize a list to store the bearish engulfing patterns
  bearish_engulfing_patterns = []
  
  # Loop through the prices and look for bearish engulfing patterns
  for i in range(1, len(prices)):
    # Check if the current day's price is a large black candlestick that completely engulfs the previous day's small white candlestick
    if prices[i]['close'] < prices[i]['open'] and prices[i]['close'] < prices[i-1]['close'] and prices[i]['open'] > prices[i-1]['open']:
      # If the pattern is found, append it to the list
      bearish_engulfing_patterns.append((i-1, i))
      
  # Return the list of bearish engulfing patterns
  return bearish_engulfing_patterns




