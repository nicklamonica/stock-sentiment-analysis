import yaml
from apis.stocks import StockData
from apis.stocktwits import StockTwitsData

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
    price_data['Close'].plot()
    print(StockTwitsData().get_comments('TSLA'))

if __name__ == '__main__':
    getData()
    print(config_loader("config.yaml"))
