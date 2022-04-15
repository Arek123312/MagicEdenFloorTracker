import requests

def getSolPrice(solana_price):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    solana_price = response['price'][:-6]