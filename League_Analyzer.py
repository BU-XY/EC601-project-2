# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:50:17 2021

@author: xy
"""

import requests
import bs4
import os
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1


author = OAuth1 (
    os.environ['api_key'],
    os.environ['api_secret'],
    os.environ['access_token'],
    os.environ['access_token_secret']
) #environment variables


url_api = "https://api.twitter.com/1.1/search/tweets.json"

q = '%40soccer -filter:retweets -filter:replies' 
league=input("Input a league:")
if league=='Bundesliga':
    q = '%40Bundesliga -filter:retweets -filter:replies' 
elif league=='laliga' or 'la liga':
    q = '%40laliga -filter:retweets -filter:replies'
elif league=='MLS':
    q = '%40MLS -filter:retweets -filter:replies'
elif league=='EPL' or 'epl' or 'Premier League':
    q = '%40EPL -filter:retweets -filter:replies'

parameters = {'q': q, 'count': 100, 'lang': 'en',  'result_type': 'recent'}
api_results = requests.get(url_api, params=parameters, auth=author)

tweets = api_results.json()

information = [BeautifulSoup(tweet['text'], 'html5lib').get_text() for tweet in tweets['statuses']]
print(information)
