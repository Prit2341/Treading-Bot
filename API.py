import requests
import json

def get_crypto_data(symbol, interval):
    base_url = "https://min-api.cryptocompare.com/data/"
    
    # Request live data
    if interval == "live":
        endpoint = f"price?fsym={symbol}&tsyms=USD"
        response = requests.get(base_url + endpoint)
        data = response.json()
        return data["USD"]
    
    # Request historical data
    else:
        endpoint = f"v2/histoday?fsym={symbol}&tsym=USD&interval={interval}"
        response = requests.get(base_url + endpoint)
        data = response.json()
        return data["Data"]

# # Example usage
# symbol = "BTC"
# interval = "day"

# live_data = get_crypto_data(symbol, "live")
# print(live_data)

# historical_data = get_crypto_data(symbol, interval)
# print(f"{symbol} price (historical, {interval}ly):")
# for data in historical_data["Data"]:
#     print(f"{data['time']:.0f}: ${data['close']}")

