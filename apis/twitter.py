import re

import requests
import pandas as pd


class Twitter:
    def __init__(self, config):
        self.key = config['api_config']['twitter']

    def get_tweets(self, ticker, start_time, end_time, interval):
        url = self.create_url(ticker)
        headers = self.create_headers()
        response = requests.request('GET', url, headers=headers).json()
        # data to pandas df
        df = pd.DataFrame.from_records(response['data'])
        # clean data
        df['text'] = df['text'].apply(self.clean_tweet)
        return df

    def clean_tweet(self, tweet):
        # remove @ mentions, hashtags, # Re-tweets # Hyper Links
        tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'RT[\s]+', '', tweet)
        tweet = re.sub(r'https?:\/\/\S+', '', tweet)
        tweet = re.sub(r'(\r\n|\n|\r)', '', tweet)
        return tweet

    def create_url(self, ticker, limit=100):
        url = f'https://api.twitter.com/2/tweets/search/recent?max_results={limit}&query={ticker}'
        return url

    def create_headers(self):
        return {"Authorization": f"Bearer {self.key}"}
