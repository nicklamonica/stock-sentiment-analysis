import yaml
import requests
#import pandas as pd
import json
import ast
from collections import Counter


def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return


if __name__ == '__main__':
    auth = requests.auth.HTTPBasicAuth("xQVhO_pVZaf_JA", "ZqXWXfLGyMy4uOKewtSOYiyUygG6iQ")

    # Data for auth
    data = {
        'grant_type' : 'password',
        'username' : 'thebmw37x',
        'password' : 'bigyeet1'
    }

    # Version of this application
    headers = {'User-Agent' : 'test/0.0.1'}

    # Getting access token
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'

    # Getting hot posts from r/wallstreetbets
    wsb_hot = requests.get('https://oauth.reddit.com/r/wallstreetbets/hot', headers=headers).json()

    # Creating list of post titles
    wsb_titles = ""

    for post in wsb_hot['data']['children']:
        wsb_titles += post['data']['title']

    split_wsb_titles = wsb_titles.split()

    # Counting instances of most popular words
    Counter = Counter(split_wsb_titles)

    # 25 most common words in the titles
    wsb_common = Counter.most_common(25)

    for word in wsb_common:
        print(word)
