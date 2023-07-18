import pandas as pd
import requests
import json
#from pandas_profiling import ProfileReport

# Load 3ridge data
df = pd.read_csv("3ridge-web.users.csv")
df.info()
df.head(2)

# Exploratory Analysis - Data profiling report
#profile = ProfileReport(df)
#profile.to_notebook_iframe()

df_wallet_0 = df["wallets[0].address"]
df_wallet_1 = df["wallets[1].address"]
df_wallet_2 = df["wallets[2].address"]

df_rewardPoint = df["rewardPoint"]
df_rewardPoint.head(20)
df_rewardPoint.info()

df_wallet_0.dropna(inplace=True)
df_wallet_0.head()
df_wallet_0.info()
df_wallet_1.head()
df_wallet_2.head()

# Ethereum wallet addresses

wallet_addresses = list(df_wallet_0)

data = []

for address in wallet_addresses:
    if address.startswith('0x'):
        data.append(["Ethereum", address])
    elif address.startswith('SP'):
        data.append(["Stacks", address])
        
print(wallet_addresses[1])

# Etherscan API endpoint and API key
api_url = "https://api.etherscan.io/api"
api_key = "WDP81QQFM85H8DN132FCJW8TFJF92YR9XG"

for address in wallet_addresses:

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
        print([ {'from': tx['from'], 'to': tx['to'], 'value': int(tx['value'])/10**18, 'timestamp': tx['timeStamp']} \
        for tx in txs ])

