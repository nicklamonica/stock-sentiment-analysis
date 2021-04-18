
class Kaggle:

    def __init__(self, conf, file):
        # load data
        pass

    def load_data(self):
        pass

    def clean_tweet(self, tweet):
        # remove @ mentions, hashtags, Re-tweets, Hyper Links, and new lines
        tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        tweet = re.sub(r'RT[\s]+', '', tweet)
        tweet = re.sub(r'https?:\/\/\S+', '', tweet)
        tweet = re.sub(r'(\r\n|\n|\r)', '', tweet)
        return tweet
