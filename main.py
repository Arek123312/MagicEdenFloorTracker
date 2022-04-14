import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey
import json
from os import path

file_path = "D:\MagicEdenFloorTracker\collections.json"

LAMPORTS = 1000000000 # number of lamports in 1 solana
totalBalance = 0
publicKey = 'ALcLZyR74AZVc6p1SJnoEyLHeViKtdtRj5xHKvsaRYzF'

#collections = ["astrals", "famous_fox_federation", "tombstoned", "tombstoned", "yaku_corp_capsulex", "yaku_corp_capsulex",
#"yaku_corp", "yaku_corp"]

f = open(file_path, 'r+')
data = json.load(f)

menu_choice = input("1. Dodaj NFT do portfolio\n2. Usuń NFT z portfolio\n3. Wyświetl aktualne portfolio\n4. Oblicz wartość portfolio\n")

match(menu_choice):
    case '1':
        listObj = []

        addName = input("Wprowadź nazwę kolekcji (np. famous_fox_federation): ")
        addAmount = int(input("Wprowadź ilość sztuk z kolekcji: "))

        new_data = {"Name":addName,
                    "Amount":addAmount
                    }

        data["Collections"].append(new_data)
        # Sets file's current position at offset.
        f.seek(0)
        # convert back to json.
        json.dump(data, f, indent = 4)
        
    case '3':
        for i in data['Collections']:
            url = "http://api-mainnet.magiceden.dev/v2/collections/" + i['Name'] + "/stats"

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload).json()

            print("Symbol: " + response['symbol'])
            print("   Amount: " + str(i['Amount']))


    case '4':
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
        results = solana_client.get_balance(PublicKey(publicKey))

        solanaBalance = results['result']['value']/LAMPORTS
        totalBalance = totalBalance * 0.91 #assuming that fee is 9%
        totalBalance += solanaBalance

        print("\nYour Solana wallet balance: " + str(solanaBalance))
        print("Total balance: " + str(totalBalance))
        




