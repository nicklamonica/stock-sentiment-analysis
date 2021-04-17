import requests
import pandas as pd

class Twitter():

    def __init__(self, config):
        self.key = config['api_config']['twitter']

    def getTweets(self, ticker, startTime, endTime, interval):
        url = self.createUrl(ticker)
        headers = self.createHeaders()
        response = requests.request('GET', url, headers=headers).json()
        # data to pandas df
        print(response['data'])
        return pd.DataFrame.from_records(response['data'])


    def createUrl(self, ticker, max=100):
        url = f'https://api.twitter.com/2/tweets/search/recent?max_results={max}&query={ticker}'
        return url

    def createHeaders(self):
        return {"Authorization": f"Bearer {self.key}"}
