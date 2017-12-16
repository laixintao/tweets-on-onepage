# -*- coding: utf-8 -*-

import tweepy


from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
#Get your Twitter API credentials and enter them here
consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_key = ACCESS_TOKEN_KEY
access_secret = ACCESS_TOKEN_SECRET

def get_tweets():
    print(consumer_key, consumer_secret)
    print(type(consumer_key))
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    print(public_tweets)


get_tweets()
