import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey

LAMPORTS = 1000000000 # number of lamports in 1 solana
totalBalance = 0
collections = ["astrals", "famous_fox_federation", "tombstoned", "tombstoned", "yaku_corp_capsulex", "yaku_corp_capsulex",
"yaku_corp", "yaku_corp"]

for i in range(0,len(collections)):
    url = "http://api-mainnet.magiceden.dev/v2/collections/" + collections[i] + "/stats"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    print("Symbol: " + response['symbol'])
    print("Floor: ", end='') 
    print(response['floorPrice']/LAMPORTS)

    totalBalance += float(response['floorPrice']/LAMPORTS)

solana_client = Client("https://api.mainnet-beta.solana.com")
results = solana_client.get_balance(PublicKey('ALcLZyR74AZVc6p1SJnoEyLHeViKtdtRj5xHKvsaRYzF'))

solanaBalance = results['result']['value']/LAMPORTS
totalBalance = totalBalance * 0.91 #assuming that fee is 9%
totalBalance += solanaBalance

print("Your Solana wallet balance: " + str(solanaBalance))
print("Total balance: " + str(totalBalance))


