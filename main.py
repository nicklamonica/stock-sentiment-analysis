# Nick Lamonica and Bryce Woods
# https://www.geeksforgeeks.org/nlp-gensim-tutorial-complete-guide-for-beginners/

import yaml
import requests
import json
import nltk
from nltk.corpus import stopwords
import gensim
from gensim import corpora
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import remove_stopwords
import numpy as np

def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return


if __name__ == '__main__':

    # Getting user input
    val = input("Enter a term: ")
    n = input("Enter the number of similar terms to generate: ")

    # Auth for Reddit API
    auth = requests.auth.HTTPBasicAuth("xQVhO_pVZaf_JA", "ZqXWXfLGyMy4uOKewtSOYiyUygG6iQ")

    # Positive and Negative words for sentiment analysis
    pos_words = ["increase", "up", "buy", "large", "largest", "gain", "gains", "gained", "like", "winner", "winners", "valuable", "moon", "high", "higher", "call", "calls", "rise", "rising", "profit", "profits", "jump", "jumped", "jumping", "growth", "hypergrowth", "love", "good", "best"]
    neg_words = ["decrease", "down", "sell", "small", "smaller", "loss", "losses", "lost", "bad", "hate", "dislike", "loser", "losers", "worthless", "low", "lower", "put", "puts", "fall", "falling", "less", "drop", "dropping", "shrunk", "negative", "worst"]

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
    # Getting hot posts from r/investing
    inv_hot = requests.get('https://oauth.reddit.com/r/investing/hot', headers=headers).json()
    # Getting hot posts from r/CryptoCurrency
    cc_hot = requests.get('https://oauth.reddit.com/r/CryptoCurrency/hot', headers=headers).json()
    # Getting hot posts from r/pennystocks
    ps_hot = requests.get('https://oauth.reddit.com/r/pennystocks/hot', headers=headers).json()

    # Creating list of post titles
    wsb_data = "|POST|"
    inv_data = "|POST|"
    cc_data = "|POST|"
    ps_data = "|POST|"

    # Appending each post to its list with a delimiter
    for post in wsb_hot['data']['children']:
        wsb_data += (post['data']['title'] + " " + post['data']['selftext'])
        wsb_data += "|POST|"

    for post in inv_hot['data']['children']:
        inv_data += (post['data']['title'] + " " + post['data']['selftext'])
        inv_data += "|POST|"

    for post in cc_hot['data']['children']:
        cc_data += (post['data']['title'] + " " + post['data']['selftext'])
        cc_data += "|POST|"

    for post in ps_hot['data']['children']:
        ps_data += (post['data']['title'] + " " + post['data']['selftext'])
        ps_data += "|POST|"

    # Creating one list with all the data
    all_data = wsb_data + inv_data + cc_data + ps_data

    # Remove stopwords
    all_data  = [word for word in all_data.split() if word.lower() not in set(stopwords.words('english'))]
    cleaned_data = ' '.join(all_data)

    # Tokenizing data
    tokenized = []
    for post in cleaned_data.split("|POST|"):
      tokenized.append(simple_preprocess(post, deacc = True))

    # Training Word2Vec model with tokenized data
    w2v_model = Word2Vec(tokenized, min_count = 0, workers = cpu_count())

    # Find most similar words to input
    most_similar = w2v_model.wv.most_similar(val, topn = int(n))

    tot_pos = 0
    tot_neg = 0

    # Output the most similar
    print("----------Similar Words----------")
    for i in most_similar:
        sentiment = ""
        if(i[0] in  pos_words):
            sentiment = "(POSITIVE SENTIMENT)"
            tot_pos += 1
        elif(i[0] in neg_words):
            sentiment = "(NEGATIVE SENTIMENT)"
            tot_neg += 1
        print(i[0] + "   " + sentiment)

    print("\n*****Sentiment Score*****")
    print("Total positive: " + str(tot_pos))
    print("Total negative: " + str(tot_neg))
    print("Aggregate Score: " + str(tot_pos - tot_neg))
