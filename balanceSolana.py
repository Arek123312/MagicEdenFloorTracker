import re
from solana.rpc.api import Client
from solana.publickey import PublicKey

LAMPORTS = 1000000000 # number of lamports in 1 solana

solana_client = Client("https://api.mainnet-beta.solana.com")
results = solana_client.get_balance(PublicKey('ALcLZyR74AZVc6p1SJnoEyLHeViKtdtRj5xHKvsaRYzF'))

print(results['result']['value']/LAMPORTS)


