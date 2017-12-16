# -*- coding: utf-8 -*-

import logging

import tweepy

from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('download')


def download_tweets():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    logger.debug('start auth...')
    api = tweepy.API(auth)

    logger.debug('start download...')
    public_tweets = api.home_timeline()

    logger.debug('saving tweets...')
    import ipdb
    ipdb.set_trace()
    with open('tweets.json', 'w+') as sample_file:
        sample_file.write(public_tweets)
    logger.info('DONE!')


if __name__ == '__main__':
    download_tweets()
