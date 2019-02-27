from twython import Twython
import json

data = open('secrets.json')
d = json.load(data)

API_KEY = d[0]["API_KEY"]
API_SECRET = d[0]["API_SECRET"]
ACCESS_TOKEN = d[0]["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = d[0]["ACCESS_TOKEN_SECRET"]

twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_client.update_status(status='Hello World!')