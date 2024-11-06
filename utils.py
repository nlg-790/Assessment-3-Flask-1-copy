import os
import requests


api_key = os.environ.get('CURRENCYLAYER_API_KEY')

def is_valid_currency(code, valid_codes):
    return code.upper() in valid_codes

def convert_currency(from_currency, to_currency, amount, api_url):
    params = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'access_key': api_key  
    }

 
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Request failed:", e)
        return None

