import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def moving_average_crossover(data, short_window, long_window):
    # Calculate the moving averages
    short_average = data.rolling(window=short_window).mean()
    long_average = data.rolling(window=long_window).mean()
    
    # Create a DataFrame to hold the signals
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']
    signals['short_average'] = short_average
    signals['long_average'] = long_average
    
    # Generate the signals
    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(signals['short_average'][short_window:] 
                                                > signals['long_average'][short_window:], 1.0, 0.0)
    
    # Calculate the trading positions
    signals['positions'] = signals['signal'].diff()
    
    # Plot the signals
    plt.figure(figsize=(15,5))
    plt.plot(signals.index, signals['price'], label='Price')
    plt.plot(signals.index, signals['short_average'], label='Short Average')
    plt.plot(signals.index, signals['long_average'], label='Long Average')
    plt.legend()
    plt.show()

# Load the data
data = pd.read_csv("D:\BOT\Testing_Area\TATASTEEL.csv")

# Call the moving_average_crossover function
moving_average_crossover(data, 50, 200)
