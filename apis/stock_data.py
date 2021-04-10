import yfinance as yf

'''
Class that gets stock data based on the ticker symbol passed in
Data clan be queried by specifying period and interval
period = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
interval = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
'''
class StockData:

    def __init__(self, ticker="TSLA"):
        self.stock = yf.Ticker(ticker)

    # ohlc = Open, High, Low, Close, or All
    def getPrice(self, period="1mo", interval="1d", ohlc="All"):
        data = self.stock.history(period=period, interval=interval)

        if ohlc== "All":
            return data.drop(['Volume', 'Dividends', 'Stock Splits'], axis=1)

        # parse out other columns except ohlc data
        return data[ohlc]

    def getVolume(self, period="1mo", interval="1d"):
        data = self.stock.history(period=period, interval=interval)
        # parse out uneeded columns
        return data.filter(['Date','Volume'])