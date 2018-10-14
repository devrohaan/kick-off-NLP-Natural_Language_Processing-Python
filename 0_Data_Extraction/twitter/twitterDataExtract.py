#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:43:48 2018

@author: Rohan

Building a corpus by accessing the Twitter Search API using Python.

"""

#   pip install tweepy

import tweepy
import time

# Create your own accound and get credentials @ https://developer.twitter.com

start_time = time.time()
# Consumer API keys
consumer_api_key = 'XXXX'
consumer_api_secret_key = 'XXXX'

# Access token & access token secret
access_token = 'XXXX'
access_token_secret = 'XXXX'

authentication = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)

## fill in your search query and store your results in a variable
tweets = api.search(q = "Cristiano Ronaldo", lang = "en", result_type = "recent", count = 10000)

## use the codecs library to write the text of the Tweets to a .txt file
file = open("CR_Tweets.txt", "w")
for tweet in tweets:
    file.write(tweet.text)
    file.write("\n")
file.close()
print(" Data Extraction Completed in %d seconds!" %(time.time() - start_time))