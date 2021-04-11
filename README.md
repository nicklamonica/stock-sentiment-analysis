# Stock Sentiment Analysis

#### Bryce Woods and Nicholas LaMonica

A stock sentiment analysis program that attempts
to predict the movements of stocks based on the prevailing sentiment from social media websites.

## How To run

1. pip install -r requirements.txt
2. change `sample_config.yaml` to `config.yaml` and fill in your api keys and other configurations
3. python main.py or run in pycharm

## Code explanation 
### Data
* The sentiment data will come from twitter and reddit APIs. 
    * https://developer.twitter.com/en/docs
    * https://www.reddit.com/dev/api/
* The stock data will come from Yahoo Finance Python API
    * https://pypi.org/project/yfinance/ 

### Data Cleaning
TBD
### Exploratory Data Analysis
TBD
### ML Models
TBD
### Results and Analysis

## Sources
* Papers:   
    * https://arxiv.org/pdf/1812.04199.pdf  
    * https://arxiv.org/pdf/1607.01958.pdf  
    * https://journalofbigdata.springeropen.com/articles/10.1186/s40537-017-0111-6
* API Docs
    * Twitter API: https://developer.twitter.com/en/docs
    * Reddit API: https://www.reddit.com/dev/api/
    * StockTwits API: https://api.stocktwits.com/developers/docs/api
    * Yahoo finance python package: https://pypi.org/project/yfinance/
    