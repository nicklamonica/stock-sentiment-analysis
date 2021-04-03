import yaml
import requests
import pandas as pd
import json
import ast
import yaml


def config_loader(filepath):
    with open(filepath, 'r') as file:
        config = yaml.load(file, Loader=yaml.BaseLoader)
    return config


if __name__ == '__main__':
    print('Hello world')
    print(config_loader("config.yaml"))
