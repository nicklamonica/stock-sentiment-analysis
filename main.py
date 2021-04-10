import requests
import pandas as pd
import json
import ast
import yaml
from apis.stock_data import StockData

def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return

def getData():
    gme = StockData(ticker="GME")
    price_data = gme.getPrice()
    print(price_data['Close'])

if __name__ == '__main__':
    getData()
    print(config_loader("config.yaml"))
