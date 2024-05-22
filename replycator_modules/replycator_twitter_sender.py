import tweepy
from cfg import tweet
import os

API_KEY = tweet.API_KEY
API_SECRET_KEY = tweet.API_SECRET
ACCESS_TOKEN = tweet.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = tweet.ACCESS_TOKEN_SECRET

try:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    api2 = tweepy.Client(consumer_key=API_KEY,
                    consumer_secret=API_SECRET_KEY,
                    access_token=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET)
except:
    print('error')

def send():
    try:
        for filename in os.listdir("files/"):
            extension = filename.split('.')[-1]
            print(extension)
            if extension == 'png' or extension == 'jpg' or extension == 'webp':
                media = api.media_upload(filename=f'files/{filename}')
                media_id = media.media_id
                api2.create_tweet(media_ids=[media_id])
            elif extension == 'txt':
                text_file = open('files/text.txt', 'r+')
                #api.update_status(text_file.read())
                api2.create_tweet(text=text_file.read())
            else:
                continue
        
        return 0
    except:
        return 1