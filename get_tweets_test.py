# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:13:34 2021

@author: xy
"""

import requests
import bs4
import os
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
from get_tweets import *


def test_too_comlicated_input(information):
    if information==[]:
        return 1
    else:
        return 0

def test_too_simple_input(word):
    if len(word)==1:
        return 1
    else:
        return 0
    
if (test_too_comlicated_input(information)==0 and test_too_simple_input(word)==0):
    print(information)
elif (test_too_comlicated_input(information)==1):
    print("Too complicated input that noone mentions")
elif (test_too_simple_input(word)==1):
    print("Too simple input that does not make any sense")