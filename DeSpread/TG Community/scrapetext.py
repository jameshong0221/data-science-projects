from telethon.sync import TelegramClient
import pandas as pd

api_id = 21533269
api_hash = "3162bbe27475795c66e3bea0438e6fae"
phone = '+821049477961'
username = 'Colajames'

data = []
with TelegramClient(username, api_id, api_hash) as client:
    for message in client.iter_messages("https://t.me/AptosKR"):
        print(message.sender_id, ':', message.text, message.date)
        data.append([message.sender_id, message.text, message.date, message.id, message.post_author,
                     message.views, message.peer_id.channel_id])

df = pd.DataFrame(data, columns = ["message.sender_id", "message.text"," message.date", "message.id",  
                                   "message.post_author", "message.views", "message.peer_id.channel_id"])

df.to_csv('aptoskorea.csv')