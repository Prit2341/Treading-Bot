import requests
import json

# Binance API endpoint for making trade requests
base_url = "https://api.binance.com"

# Binance API endpoint for getting the current ETH market price
eth_price_url = f"{base_url}/api/v3/ticker/price?symbol=ETHUSDT"

# Binance API key and secret
api_key = "auzL17Z7gkTeJD564A3lcTgUobC1KUWGchWjNRL53F1eYJxM2Rlw5q3cmlWsT7J0"
api_secret = "gDldf7Z2AlUfkIyiMdCHJSu32C7xf1FCwrk7miSmNqB1jJDqBZungDq9mC25hVEL"

# Get the current ETH market price
eth_price_response = requests.get(eth_price_url)
eth_price_data = json.loads(eth_price_response.text)
eth_price = float(eth_price_data["price"])

# Function to buy ETH at the market price
def buy_eth():
    # Construct the buy order payload
    buy_payload = {
        "symbol": "ETHUSDT",
        "side": "BUY",
        "type": "MARKET",
        "quantity": "0.0001"
    }

    # Add the API key and signature to the headers
    headers = {
        "X-MBX-APIKEY": api_key
    }

    # Send the buy order to the Binance API
    buy_response = requests.post(f"{base_url}/api/v3/order", json=buy_payload, headers=headers)
    print(buy_response.text)

# Function to sell ETH at the market price
def sell_eth():
    # Construct the sell order payload
    sell_payload = {
        "symbol": "ETHUSDT",
        "side": "SELL",
        "type": "MARKET",
        "quantity": "0.0001"
    }

    # Add the API key and signature to the headers
    headers = {
        "X-MBX-APIKEY": api_key
    }

    # Send the sell order to the Binance API
    sell_response = requests.post(f"{base_url}/api/v3/order", json=sell_payload, headers=headers)
    print(sell_response.text)
