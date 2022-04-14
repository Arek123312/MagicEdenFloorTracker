from msilib.schema import Error
from operator import truediv
from typing import Collection
import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey
import json
from os import path

file_path = "D:\MagicEdenFloorTracker\collections.json"

LAMPORTS = 1000000000 # number of lamports in 1 solana
totalBalance = 0
#publicKey = 'ALcLZyR74AZVc6p1SJnoEyLHeViKtdtRj5xHKvsaRYzF'

#collections = ["astrals", "famous_fox_federation", "tombstoned", "tombstoned", "yaku_corp_capsulex", "yaku_corp_capsulex",
#"yaku_corp", "yaku_corp"]

active = True

while(active):
    menu_choice = input("1. Dodaj NFT do portfolio\n2. Usuń NFT z portfolio\n3. Wyświetl aktualne portfolio\n4. Oblicz wartość portfolio\n5. Wprowadź adres Solana \n6. Wyjdź \n")
    match(menu_choice):
        case '1':
            f = open('collection.json', 'r+')
            data = json.load(f)

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
            f.close()
            
        
        case '2':
            f = open('collection.json', 'r')
            data = json.load(f)
            print(data)
            f.close()
        
            delete = input("Którą kolekcję chcesz usunąć?: ")
            delete_data = {"Name": delete}

            j = 0
            for i in data['Collections']:
                if i['Name'] == delete:
                    del data['Collections'][j]
                j += 1
            
            f = open('collection.json', 'w')
            json.dump(data, f, indent = 4)
            print(data)
            f.close()
            

        case '3':
            f = open('collection.json', 'r')
            data = json.load(f)
            for i in data['Collections']:
                url = "http://api-mainnet.magiceden.dev/v2/collections/" + i['Name'] + "/stats"

                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload).json()

                print("Symbol: " + response['symbol'])
                print("   Amount: " + str(i['Amount']))
                f.close()


        case '4':
            totalBalance = 0
            solanaBalance = 0
            f = open('collections.json', 'r')
            data = json.load(f)
            for i in data['Collections']:
                url = "http://api-mainnet.magiceden.dev/v2/collections/" + i['Name'] + "/stats"

                payload={}
                headers = {}

                try:
                    response = requests.request("GET", url, headers=headers, data=payload).json()

                    print("Symbol: " + response['symbol'])
                    print("Floor: ", end='') 
                    print(response['floorPrice']/LAMPORTS, end='')
                    print("   Amount: " + str(i['Amount']))
                except Exception:
                    print("Nie wykryto kolekcji. Sprawdź poprawność danych!")
                    break
                totalBalance += float(response['floorPrice']/LAMPORTS) * i['Amount']
            
            f2 = open('wallet.txt', 'r')
            publicKey = f2.read()
            solana_client = Client("https://api.mainnet-beta.solana.com")
            results = solana_client.get_balance(PublicKey(publicKey))

            solanaBalance = results['result']['value']/LAMPORTS
            totalBalance = totalBalance * 0.91 #assuming that fee is 9%
            totalBalance += solanaBalance

            print("Your NFT total floor value: " + str(totalBalance))
            print("\nYour Solana wallet balance: " + str(solanaBalance))
            print("Total balance: " + str(totalBalance))
            print("")
            f.close()

        case '5':
            publicKey = input('Wprowadź adres portfela: \n')

            f = open('wallet.txt', 'w')
            f.write(publicKey)
            f.close()

        case '6':
            active = False
                

            
        




