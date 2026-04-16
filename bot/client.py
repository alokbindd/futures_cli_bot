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



