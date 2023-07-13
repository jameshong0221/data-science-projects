import pandas as pd
import requests

df = pd.read_csv("3ridge-web.users.csv")
df.info()
df.head()

df_wallet_0 = df["wallets[0].address"]
df_wallet_1 = df["wallets[1].address"]
df_wallet_2 = df["wallets[2].address"]

df_wallet_0.dropna(inplace=True)
df_wallet_0.head()
df_wallet_1.head()
df_wallet_2.head()

# Ethereum wallet addresses
wallet_addresses = list(df_wallet_0)
print(wallet_addresses[1])
# Etherscan API endpoint and API key
api_url = "https://api.etherscan.io/api"
api_key = "WDP81QQFM85H8DN132FCJW8TFJF92YR9XG"

for address in wallet_addresses:
    if not address.startswith('0x'):
        print(address)
# Iterate through wallet addresses and save as list
for address in wallet_addresses:
    # Construct the API request URL
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "apikey": api_key,
    }
    
    # Send API request
    response = requests.get(api_url, params=params)
    
    # Parse the API response
    data = response.json()
    balance = int(data["result"]) / 10**18  # Convert balance from wei to ether
    
    # Print the balance
    print(f"Address: {address}")
    print(f"Balance: {balance} ETH")
    print("---")
