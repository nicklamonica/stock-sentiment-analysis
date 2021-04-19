import yaml
import pandas as pd

from apis.twitter import Twitter
from models.rnn import RNN

def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return None


def main():
    rnn = RNN()
    # t = Twitter()
    # data = t.get_tweets("TSLA")
    # rnn.driver(data)


if __name__ == '__main__':
    main()
