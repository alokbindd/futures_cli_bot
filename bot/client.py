import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

def get_client():
    client = Client(api_key=API_KEY, api_secret=API_SECRET_KEY)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    return client

def get_current_price(client, symbol):
    try:
        ticker = client.futures_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
    except Exception as e:
        raise Exception(f"Failed to fetch current price: {str(e)}")
