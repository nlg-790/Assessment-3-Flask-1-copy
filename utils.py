import os
import requests

# Retrieve API key from environment variable
api_key = os.environ.get('EXCHANGE_API_KEY')

def is_valid_currency(code, valid_codes):
    return code.upper() in valid_codes

def convert_currency(from_currency, to_currency, amount, api_url):
    params = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount
    }

    # Include the API key in the request if it's available
    if api_key:
        params['apikey'] = api_key

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None
