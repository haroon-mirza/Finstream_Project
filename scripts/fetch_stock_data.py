import requests
import time
import json

# api parameters
api_key = "alpha_vantage_key"
base_url = "https://www.alphavantage.co/query"

# Stocks list
stock_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "FB", "TSLA", "BRK.B", "NVDA", "JPM",
    "JNJ", "V", "PG", "UNH", "DIS", "MA", "HD", "BAC", "PYPL", "CMCSA", "XOM", "VZ",
    "ADBE", "CSCO", "KO", "NFLX", "PFE", "MRK", "PEP", "T", "INTC", "CRM", "ABT", 
    "ORCL", "ABBV", "LLY", "COST", "MCD", "DHR", "MDT", "BMY", "NEE", "PM", "WMT", 
    "QCOM", "TXN", "HON", "ACN", "LIN", "AVGO", "SBUX", "LOW", "IBM", "MMM", "BA"]

# loop through each and fetch data
for symbol in stock_symbols:
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": api_key
    }

    # calling the api
    response = requests.get(base_url, params=params)
    data = response.json()

    # extract last data point
    latest_data = list(data["Time Series (5min)"].values())[0]
    print(f"Latest data for {symbol} at {list(data['Time Series (5min)'].keys())[0]}: {latest_data}")

# waiting 12 seconds to avoid the rate limit (5 requests per minute)
time.sleep(12)