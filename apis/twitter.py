import re
import requests
import pandas as pd
from searchtweets.api_utils import convert_utc_time


class Twitter:
    def __init__(self, config):
        self.key = config['api_config']['twitter']
        self.base_url = 'https://api.twitter.com/2/tweets/search/all'

    # date must be in YYYY-MM-DDTHH:mm:ss
    def get_tweets(self, ticker, date_since='2019-04-15T00:00:00', date_until='2021-04-16T00:00:00', limit=100):
        headers = self.create_headers()
        params = self.create_params(ticker, date_since, date_until, limit)
        response = requests.request('GET', self.base_url, headers=headers, params=params).json()
        # data to pandas df
        print(response)
        # df = pd.DataFrame.from_records(response['data'])
        # # clean data
        # df['clean_text'] = df['text'].apply(self.clean_tweet)
        return df

    def clean_tweet(self, tweet):
        # remove @ mentions, hashtags, Re-tweets, Hyper Links, and new lines
        tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'RT[\s]+', '', tweet)
        tweet = re.sub(r'https?:\/\/\S+', '', tweet)
        tweet = re.sub(r'(\r\n|\n|\r)', '', tweet)
        return tweet

    def create_params(self, ticker, date_since, date_until, limit):
        # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
        # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
        query_params = {
            'query': f'(from:${ticker} -is:retweet) OR #{ticker}',
            'tweet.fields': 'id,created_at,text',
            'start_time': date_since,
            'end_time': date_until,
            'max_results': limit
        }
        return query_params

    def create_headers(self):
        return {"Authorization": f"Bearer {self.key}"}

    def utc_convert(self, time):
        pass
