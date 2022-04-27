import json
from re import X
import requests
from typing import Collection
import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey
from os import path
from datetime import datetime

from binance_api import getSolPrice
from usd_price_api import getUsdPrice

LAMPORTS = 1000000000 # number of lamports in 1 solana

def function1():
            f = open('collections.json', 'r+')
            data = json.load(f)

            try:
                addName = input("Wprowadź nazwę kolekcji (np. famous_fox_federation): ")
                addAmount = int(input("Wprowadź ilość sztuk z kolekcji: \n"))
                new_data = {"Name":addName,
                            "Amount":addAmount
                        }

                data["Collections"].append(new_data)
                # Sets file's current position at offset.
                f.seek(0)
                # convert back to json.
                json.dump(data, f, indent = 4)
                f.close()
            except Exception:
                print('\033[1m'+"\nWprowadzono złą wartość dla liczby sztuk!\n" + '\033[0m')

def function2():
            collection_list = []
            f = open('collections.json', 'r')
            data = json.load(f)
            print("\nDostępne kolekcje: ")
            for i in data['Collections']:
                print(i['Name'])
                collection_list.append(i['Name'])
            f.close()

            delete = input("Którą kolekcję chcesz usunąć?: ")
            if delete in collection_list:
                print("Pomyślnie usunięto {}\n".format(delete))
            else:
                print('\033[1m'+ "Nie ma takiej kolekcji!\n" + '\033[0m')
            #delete_data = {"Name": delete}

            j = 0
            for i in data['Collections']:
                if i['Name'] == delete:
                    del data['Collections'][j]
                j += 1
            
            f = open('collections.json', 'w')
            json.dump(data, f, indent = 4)
            f.close()
            

def function3():
            f = open('collections.json', 'r')
            data = json.load(f)
            for i in data['Collections']:
                url = "http://api-mainnet.magiceden.dev/v2/collections/" + i['Name'] + "/stats"

                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload).json()

                print("Symbol: " + response['symbol'])
                print("   Ilość: " + str(i['Amount']))
                f.close()
            print('\n')

def function4():
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
                    continue
                totalBalance += float(response['floorPrice']/LAMPORTS) * i['Amount']
            
            try:
                f2 = open('wallet.txt', 'r')
                publicKey = f2.read()
                solana_client = Client("https://api.mainnet-beta.solana.com")
                results = solana_client.get_balance(PublicKey(publicKey))
                solanaBalance = results['result']['value']/LAMPORTS
            except Exception:
                print('\033[1m'+ "Wprowadzono zły adres Solana!\n" + '\033[0m')
                solanaBalance = 0
            
            totalBalance = totalBalance * 0.91 #assuming that the average fee is 9%
            nftBalance = totalBalance
            totalBalance += solanaBalance

            sol_price = float(getSolPrice())
            usd_price = float(getUsdPrice())
            
            print("\nSolana price: $" + str(round(sol_price, 2)))
            print("Your NFT total floor value: " + str(round(nftBalance, 2)) + ' = $' + str(round(sol_price * nftBalance, 2)))
            print("Your Solana wallet balance: " + str(round(solanaBalance, 2)) + ' = $' + str(round(sol_price * solanaBalance, 2)))
            usd_value = round(sol_price * totalBalance, 2)
            pln_value = round(usd_value * usd_price, 2)
            print("PLN/USD: " + str(usd_price))
            print("Total balance: " + str(round(totalBalance, 2)) + ' = $' + str(usd_value) + ' = PLN ' + str(pln_value))
            print("")
            history_data = "Total balance: " + str(round(totalBalance, 2)) + ' = $' + str(usd_value) + ' = PLN ' + str(pln_value)
            function6(history_data)
            f.close()

def function5():
            publicKey = input('Wprowadź adres portfela: \n')

            f = open('wallet.txt', 'w')
            f.write(publicKey)
            f.close()


def function6(balance):
            f = open('history.json', 'r+')
            data = json.load(f)

            try:
                now = datetime.now()
                now = now.strftime("%d/%m/%Y %H:%M:%S")
                total_balance = balance
                new_data = {"Date":now,
                            "Balance":total_balance
                        }

                data["History"].append(new_data)
                # Sets file's current position at offset.
                f.seek(0)
                # convert back to json.
                json.dump(data, f, indent = 4)
                f.close()
            except Exception:
                print('\033[1m'+"\nWprowadzono złą wartość!\n" + '\033[0m')


