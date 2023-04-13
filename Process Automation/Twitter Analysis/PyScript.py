import configparser
import tweepy
from tweepy import API, Cursor, OAuthHandler, TweepyException

#Read in configs
configs = configparser.ConfigParser()
configs.read(r'C:\Users\youngjames0221\Documents\Personal\Coding\config.ini')
keys = configs['TWITTER']
consumer_key = keys['CONSUMER_KEY']
consumer_secret = keys['CONSUMER_SECRET']
access_token = keys['ACCESS_TOKEN']
access_secret = keys['ACCESS_SECRET']

#Authenticate Tweepy connection to Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = API(auth, wait_on_rate_limit=True)

screen_name = 'Laboon Alliance'
ids = []
for fid in Cursor(api.get_follower_ids, screen_name=screen_name, count=5000).items():
    ids.append(fid)