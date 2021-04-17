import yaml
from apis.twitter import Twitter

def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return

if __name__ == '__main__':
    conf = config_loader("config.yaml")
    t = Twitter(conf['api_config'])
    data = t.getTweets('TSLA', 1, 1, 1)
    print(data)
