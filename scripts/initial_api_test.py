import requests
from dotenv import load_dotenv
import os

load_dotenv()
alpha_vantage_key = os.getenv('alpha_vantage_key')

# Calling the API
api_endpoint = 'https://api.bestbuy.com/v1/products((categoryPath.id=abcat0502000))'
params = {
    'apiKey': 'YOUR_API_KEY_HERE',
    'format': 'json',
    'pageSize': 5
}

# API Call
response = requests.get(api_endpoint, params=params)

# Run
if response.status_code == 200:
    data = response.json()
    print('API call successful. Data received:', data)
else:
    print('API call failed. Status code:', response.status_code)
