import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey
import json

file_path = "D:\MagicEdenFloorTracker\collections.json"

LAMPORTS = 1000000000 # number of lamports in 1 solana
totalBalance = 0

#collections = ["astrals", "famous_fox_federation", "tombstoned", "tombstoned", "yaku_corp_capsulex", "yaku_corp_capsulex",
#"yaku_corp", "yaku_corp"]

f = open(file_path, 'r')
data = json.load(f)


for i in data['Collections']:
    url = "http://api-mainnet.magiceden.dev/v2/collections/" + i['Name'] + "/stats"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    print("Symbol: " + response['symbol'])
    print("Floor: ", end='') 
    print(response['floorPrice']/LAMPORTS, end='')
    print("   Amount: " + str(i['Amount']))

    totalBalance += float(response['floorPrice']/LAMPORTS) * i['Amount']

solana_client = Client("https://api.mainnet-beta.solana.com")
results = solana_client.get_balance(PublicKey('ALcLZyR74AZVc6p1SJnoEyLHeViKtdtRj5xHKvsaRYzF'))

solanaBalance = results['result']['value']/LAMPORTS
totalBalance = totalBalance * 0.91 #assuming that fee is 9%
totalBalance += solanaBalance

print("\nYour Solana wallet balance: " + str(solanaBalance))
print("Total balance: " + str(totalBalance))


