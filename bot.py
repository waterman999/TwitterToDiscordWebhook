import tweepy
import os
import re
import discord
import requests
import time
from discord_webhook import DiscordWebhook

url1 = 'https://discord.com/api/webhooks/825848374364078131/xR0BMvCXrGX3SddqwTvjSiN-DNNpkmJIyosTPg1n17SaxHzvILhTC8ge7p4rlQjxlcDm'
url2 = 'https://discord.com/api/webhooks/843031560390574080/UETv33YPfIVJZB0uRDULO2mbA1tlqAh3-KbBYFg03cOYRzsGOm0IthlbdSNs13xpg4s0'
url3 = 'https://discord.com/api/webhooks/843031926663151617/NCsyVo10P7SxWumjqyVfBXEvKVfhZOSsinNPaTFtVdTVtUiz2K7e1tKyAC0TMCuLBtA4'

Token = '2fFgFg9zjWBYYTeGmBBiqix70'
consumer_key = 'xY8AC4SNbF6hmN5BWXA3OkD3Q'
consumer_secret = 'QdCmGAuPTRO1RFs1jeQDYIxUrJQagAD1kp7gpR4ns9Qwx9bbNi'
access_token = '1390990681758343168-KPPfyDo5H9PmMG4RIhqHqy3UTCcFWL'
access_token_secret = 'qbWksk80sjrJTKHGuwPKzTEmr84zvkZnJgCmDKIBsgw0E'

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
   
