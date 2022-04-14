import requests

LAMPORTS = 1000000000 # number of lamports in 1 solana

collection = str(input('Wprowadź nazwę kolekcji: '))

url = "http://api-mainnet.magiceden.dev/v2/collections/" + collection + "/stats"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()

print("Floor: ", end='') 
print(response['floorPrice']/LAMPORTS)


