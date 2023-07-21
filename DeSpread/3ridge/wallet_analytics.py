import pandas as pd
import numpy as np
import requests
import json

# Etherscan API endpoint and API key
api_url_evm = "https://api.etherscan.io/api"
api_key = "WDP81QQFM85H8DN132FCJW8TFJF92YR9XG"

# Hiro API endpoint
api_url_stx = "https://api.mainnet.hiro.so/extended/v1/" + stx_address + "/SP37SE3P6RHC8FKDZC46E8C2A39S7ZSFKS569AJV4/transactions"

# Load 3ridge data
df = pd.read_csv("user_data.csv")
df['wallets[0].address']

tx_cnt = []

for wallet00 in df['wallets[0].address']:
    
    # EVM
    if wallet00.startswith('0x'):
        params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 10,
        "sort": 'asc',
        "apikey": api_key,
        }
        response = requests.get(api_url_evm, params=params)
        data = response.json()
        tx_cnt.append(len(data['result']))    # Tx count

    # Hiro
    elif wallet00.startswith('SP'):
        params = {
        "limit": 50,
        "offset": 0,
        "until_block" :999999
        }
        response = requests.get(api_url_stx, params=params)
        data = response.json()
        tx_cnt.append(data['total']) # Tx count
    
    else:
        continue


response = requests.get(api_url_stx, params=params)
data = response.json()

print(data.keys())
data['total']
print(data['results'])

print(data['results'][0].keys())
print(data['results'][1].keys())
print(data['total']) #transaction count
print(data['results'][0]['event_count'])



df_wallet_0 = df["wallets[0].address"]

df_wallet_0.dropna(inplace=True)
df_wallet_0.head()
df_wallet_0.info()

# Ethereum wallet addresses, get transaction history, balance, count
wallet_addresses = list(df_wallet_0)

data = []

for address in wallet_addresses:
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "apikey": api_key,
    }
    if address.startswith('0x'):
        response = requests.get(api_url, params=params)
        data.append([address, ])
    elif address.startswith('SP'):
        data.append(["Stacks", address])
        
print(wallet_addresses[1])

# Iterate through wallet addresses and save as list
for address in wallet_addresses:
    # Construct the API request URL
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "apikey": api_key,
    }
    if address.startswith('0x'):
        # Send API request
        response = requests.get(api_url, params=params)
    
        # Parse the API response
        data = response.json()
        balance = int(data["result"]) / 10**18  # Convert balance from wei to ether
    
        # Print the balance
        print(f"Address: {address}")
        print(f"Balance: {balance} ETH")
        print("---")

# Return transaction history of wallet address


data = []

for address in wallet_addresses:
    # Construct the API request URL
    params = {
        "module": "account",
        "action": "txlist",
        "address": "0x5320dE0613d96B4177dd0302D04074eAc37F7472",
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 10,
        "sort": 'asc',
        "apikey": api_key,
    }
    if address.startswith('0x'):
        response = requests.get(api_url, params=params)
        response_parsed = json.loads(response.content)
        txs = response_parsed['result']
        data.append([ tx['from'], tx['to'], int(tx['value'])/10**18, tx['timeStamp'] \
        for tx in txs ])

# Transaction count for each address
for address in wallet_addresses:
    # Construct the API request URL
    params = {
        "module": "proxy",
        "action": "eth_getTransactionCount",
        "address": address,
        "apikey": api_key,
    }
    if address.startswith('0x'):
        # Send API request
        response = requests.get(api_url, params=params)
    
        # Parse the API response
        data = response.json()
        tx_count = data["result"]
    
        # Print the balance
        print(f"Address: {address}")
        print(f"Tx Count: {tx_count} ")
        print("---")


api_url_evm = "https://api.etherscan.io/api"
api_key = "WDP81QQFM85H8DN132FCJW8TFJF92YR9XG"

params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 10,
        "sort": 'asc',
        "apikey": api_key,
    }

response = requests.get(api_url_evm, params=params)
data = response.json()
len(data['result'])

