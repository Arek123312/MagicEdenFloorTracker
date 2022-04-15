import requests

#def getSolPrice():
    url = "http://api.nbp.pl/api/exchangerates/rates/a/usd/"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()
    usd_price = response['rates'][0]['mid']
    print(usd_price)

    #solana_price = response['price'][:-6]
   #return solana_price