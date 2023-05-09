from telethon.sync import TelegramClient
import datetime
import pandas as pd


import configparser
config = configparser.ConfigParser()
config.read("telethon.config")

api_id = config["telethon_credentials"]["api_id"]
api_hash = config["telethon_credentials"]["api_hash"]

chats = ['cryptodubai7', 'Verasity_Official']


client =  TelegramClient('test', api_id, api_hash)


df = pd.DataFrame()


for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        for message in client.iter_messages(chat, offset_date=datetime.date.today() , reverse=True):
            print(message)
            data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date}

            temp_df = pd.DataFrame(data, index=[1])
            df = df.append(temp_df)

df['date'] = df['date'].dt.tz_localize(None)

df.to_excel("C:\\crypto\\data_{}.xlsx".format(datetime.date.today()), index=False)