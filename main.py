import yaml
import requests
import pandas as pd
import json
import ast
import yaml


def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return


if __name__ == '__main__':
    print('Hello world')
    print(config_loader("config.yaml"))
