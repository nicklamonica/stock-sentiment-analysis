import requests

class StockTwitsData:
    def __init__(self):
        self.base_url = "https://api.stocktwits.com/api/2/"
        self.headers = {'Content-Type': 'application/json'}

    # DOCS: https://api.stocktwits.com/developers/docs/api#streams-symbol-docs
    def get_comments(self, ticker, since=0, max=0, limit=30, filter=None):
        full_url = self.base_url + f'streams/symbol/{ticker}.json'
        params = {
            'since': f'{since}',
            'max': f'{max}',
            'limit': f'{limit}',
            'filter': f'{filter}'
        }
        response = requests.get(full_url, headers=self.headers, params=params).json()
        messages = response['messages']
        comments = [ message['body'] for message in messages ]
        return comments