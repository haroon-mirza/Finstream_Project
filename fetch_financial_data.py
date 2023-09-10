import boto3
import requests
import json
import time

def fetch_stock_data(symbol):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()

def transform_stock_data(data):
    try:
        latest_data = list(data["Time Series (5min)"].values())[0]
        return json.dumps(latest_data)
    except KeyError:
        print(f"KeyError: 'Time Series (5min)' not found in data.")
        return None

def load_to_s3(data, symbol):
    s3 = boto3.client('s3')
    s3.put_object(Body=data, Bucket='finstream-raw', Key=f'raw/{symbol}.json')

if __name__ == "__main__":
    stock_symbols = ["AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "FB", "TSLA", "BRK.B", "NVDA", "JPM",
    "JNJ", "V", "PG", "UNH", "DIS", "MA", "HD", "BAC", "PYPL", "CMCSA", "XOM", "VZ",
    "ADBE", "CSCO", "KO", "NFLX", "PFE", "MRK", "PEP", "T", "INTC", "CRM", "ABT", 
    "ORCL", "ABBV", "LLY", "COST", "MCD", "DHR", "MDT", "BMY", "NEE", "PM", "WMT", 
    "QCOM", "TXN", "HON", "ACN", "LIN", "AVGO", "SBUX", "LOW", "IBM", "MMM", "BA"]
    
    for symbol in stock_symbols:
        data = fetch_stock_data(symbol)
        transformed_data = transform_stock_data(data)
        if transformed_data:
            load_to_s3(transformed_data, symbol)
        time.sleep(12)  
