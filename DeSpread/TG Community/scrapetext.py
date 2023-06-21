from telethon.sync import TelegramClient
import pandas as pd

api_id = 21533269
api_hash = "3162bbe27475795c66e3bea0438e6fae"
phone = '+821049477961'
username = 'Colajames'

data = []
with TelegramClient(username, api_id, api_hash) as client:
    for message in client.iter_messages