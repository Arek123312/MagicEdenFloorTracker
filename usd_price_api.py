import requests

def getUsdPrice():
    url = "http://api.nbp.pl/api/exchangerates/rates/a/usd/"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    usd_price = round(response['rates'][0]['mid'], 2)
    return usd_price
