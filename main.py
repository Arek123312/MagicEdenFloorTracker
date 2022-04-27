from msilib.schema import Error
from operator import truediv
import time
from typing import Collection
import requests
from solana.rpc.api import Client
from solana.publickey import PublicKey
import json
import cffi
from os import path

from functions import function1, function2, function3, function4, function5, function7


LAMPORTS = 1000000000 # number of lamports in 1 solana
totalBalance = 0

active = True

f = open('collections.json', 'r+')
try:
    data = json.load(f)
except Exception:
    f.seek(0)
    f.truncate()
    f2 = open('collections_default.json', 'r+')
    default_data = f2.read()
    f2.close()
    f.write(default_data)
    f.close()
    f = open('collections.json', 'r')
    data = json.load(f)




while(active):
    menu_choice = input("1. Dodaj NFT do portfolio\n2. Usuń NFT z portfolio\n3. Wyświetl aktualne portfolio\n4. Oblicz wartość portfolio\n5. Wprowadź adres Solana \n6. Wyświetl historię\n7. Wyjdź \n\n")
    match(menu_choice):
        case '1':
            function1()

        case '2':
            function2()
            
        case '3':
            function3()

        case '4':
            function4()

        case '5':
            function5()

        case '6':
            function7()   
        case '7':
            active = False
        
        
                

            
        




