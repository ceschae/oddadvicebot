from twython import Twython
from random import shuffle
import json
import time

data = open('secrets.json')
d = json.load(data)

API_KEY = d[0]['API_KEY']
API_SECRET = d[0]['API_SECRET']
ACCESS_TOKEN = d[0]['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = d[0]['ACCESS_TOKEN_SECRET']

twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

while True:
    t = time.localtime(time.time())
    if t.tm_min % 15 == 0:
        with open('tweets.json', 'r+') as f:
            tweets = json.load(f)
            shuffle(tweets)
            index = 0
            tweeted = False
            while index != len(tweets):
                if 'tweeted' not in tweets[index]:
                    twitter_client.update_status(status=tweets[index]['tweet'])
                    tweets[index]['tweeted'] = True
                    index = len(tweets)
                    tweeted = True
                    f.seek(0)
                    json.dump(tweets, f, indent=4)
                    f.truncate()
                else:
                    index += 1
            if not tweeted: # out of tweets
                exit()
    time.sleep(60)