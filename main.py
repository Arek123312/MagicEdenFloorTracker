import requests

url = "http://api-mainnet.magiceden.dev/v2/collections/degods/stats"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

stats = response.text
print(stats)

#commit

