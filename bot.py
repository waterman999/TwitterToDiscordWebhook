import tweepy
import os
import re
import discord
import requests
import time
from discord_webhook import DiscordWebhook

url1 = 'insert here'
url2 = 'insert here'
url3 = 'insert here'

Token = 'insert here'
consumer_key = 'insert here'
consumer_secret = 'insert here'
access_token = 'insert here'
access_token_secret = 'insert here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for tweet in tweepy.Cursor(api.user_timeline, id='829790759809335296').items(2):
  if tweet.text.startswith("RT @") == True: 
    print('This tweet is a retweet')
  else:
    tweet2 = tweet.text.replace("#PogoConnection ","")
    tweet3 = tweet2.rsplit("\n",1)[0]
    tweet4 = (tweet3 + " #Join #PogoConnection")
    print(tweet4)
    tweet5 = tweet3.split("\n",3)[3]
    tweet6 = tweet3.rsplit("\n",1)[0]
    tweet7= ("```  " + tweet5 + "  ```")
    webhook = DiscordWebhook(url=url1, content=tweet6)
    #webhook2 = DiscordWebhook(url=url2, content=tweet6)
    #webhook3 = DiscordWebhook(url=url3, content=tweet6)
    response = webhook.execute()
    #response = webhook2.execute()
    #response = webhook3.execute()
    webhook = DiscordWebhook(url=url1, content=tweet7)
    #webhook2 = DiscordWebhook(url=url2, content=tweet7)
    #webhook3 = DiscordWebhook(url=url3, content=tweet7)
    response = webhook.execute()
    #response = webhook2.execute()
    #response = webhook3.execute()
   
