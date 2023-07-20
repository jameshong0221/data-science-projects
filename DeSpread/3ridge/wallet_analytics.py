import pandas as pd
import requests
import json
#from pandas_profiling import ProfileReport

# Etherscan API endpoint and API key
api_url = "https://api.etherscan.io/api"
api_key = "WDP81QQFM85H8DN132FCJW8TFJF92YR9XG"

# Load 3ridge data
df = pd.read_csv("user_data.csv")
df.info()
df.head(2)


def get_balance(wallet_address, chain):
    
for address in df["wallets[0].address"]:
    if i == 5:
        break
    print(abc)
    i += 1

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
        "address": address,
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