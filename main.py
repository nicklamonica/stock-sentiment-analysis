import yaml
from apis.twitter import Twitter


def config_loader(filepath):
    try:
        with open(filepath, 'r') as file:
            config = yaml.load(file, Loader=yaml.BaseLoader)
            return config
    except:
        print("You need a config.yaml file. Refer to the readme.md")
        return None


def main():
    conf = config_loader("config.yaml")
    t = Twitter(conf)
    data = t.get_tweets('TSLA', 1, 1, 1)
    print(data)


if __name__ == '__main__':
    main()
