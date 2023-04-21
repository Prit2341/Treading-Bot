import requests
import json

url = "https://twelve-data1.p.rapidapi.com/stocks"

querystring = {"exchange":"NASDAQ","format":"json"}

headers = {
	"X-RapidAPI-Key": "867fcb8387msh034f2da34f91894p1015dbjsn0af672c8f15a",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = response.json()

# Open JSON file in append mode
with open('data.json', 'a') as file:
    # Write data to file
    json.dump(data, file)
    # Add newline for next append
    file.write('\n')
