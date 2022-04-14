import requests

LAMPORTS = 1000000000 # number of lamports in 1 solana

url = "http://api-mainnet.magiceden.dev/v2/collections/degods/stats"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(response['floorPrice']/LAMPORTS)

#commit

