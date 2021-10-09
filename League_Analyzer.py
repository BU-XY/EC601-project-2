# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:50:17 2021

@author: xy
"""

import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1

author_info = {
    'api_key':'lGhEtjifVUr7xyM7U6xrD8EqQ',
    'api_secret':'WNc81uNSrSH5vzqT93pSAjtFdVivSt3zOBYaaIN6C4qwJpe4s5',
    'access_token':'1441894841265262595-ZNbKjnV8LIQCz0C6ntVHpXGoOKPJ5j',
    'access_token_secret':'T18zEtLLq1JoqoPVLeE56TLb1WVOC5qCge6NS7NFJDvHZ'
}


author = OAuth1 (
    author_info['api_key'],
    author_info['api_secret'],
    author_info['access_token'],
    author_info['access_token_secret']
)


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