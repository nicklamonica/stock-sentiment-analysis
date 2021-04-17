import requests
import yaml

class Twitter():

    def __init__(self, config):
        self.key = config['twitter']

    def getTweets(self, ticker, startTime, endTime, interval):
        url = self.createUrl(ticker)
        headers = self.createHeaders()
        data = requests.request('GET', url, headers=headers)
        return data.json()

    def createUrl(self, ticker, max=100):
        url = f'https://api.twitter.com/2/tweets/search/recent?max_results={max}&query={ticker}'
        return url

    def createHeaders(self):
        return {"Authorization": f"Bearer {self.key}"}
