# Stock Sentiment Analysis

#### Bryce Woods and Nicholas LaMonica

A stock sentiment analysis program that attempts
to predict the movements of stocks based on the prevailing sentiment from social media websites (twitter, reddit and stocktwits).  
Each Tweet will be given a bullish, neutral, or bearish sentiment. Every Tweet's sentiment within a certain time 
period will be averaged to give the stocks total sentiment for that time period.

## Directions to Run

1. `pip install -r requirements.txt`
2. Change `sample_config.yaml` to `config.yaml` and fill in your api keys and other configurations.
3. Run `python main.py`

## Code explanation 
### Data
* The sentiment data will come from Twitter API. 
    * https://developer.twitter.com/en/docs
* The stock data will come from Yahoo Finance Python API
    * https://pypi.org/project/yfinance/
* Right now we are using tweet data from kaggle to train the ML model for now, and use the Twitter API later for further testing.

### Data Cleaning
We clean the tweets by removing the @ mentions, hashtags, ticker symbols, and other
unneeded symbols that don't have an effect on the sentiment of a tweet.   
Also need a way to ignore tweets from bots and only use users. 
Twitter API has a way to tell if a tweet was made from a phone app, web client, or from the API.

### Exploratory Data Analysis
Ratio of positive to negative tweets, average tweet length. 

### ML Model
* We will be use Recurrent Neural Nets, specifically LSTM and GRU version of Recurrent Neural Nets. LSTM and GRU are optimized versions of regular RNNs.  
* We are using RNNs because they are good at adapting to sequence of data for predictions where the order of that data matters. 
* RNNs are  commonly used in time series data, this is perfect for our use case because we are analyzing the sentiment of the tweets overtime.  
* RNNs are also good for natural language processing because the order of the words that were written carries significance in predicting sentiment.

### Results and Analysis
I want a confusion matrix and an accuracy and loss by epoch. We can calculate the accuracy and loss by using the confusion matrix.

### What else is left?
* Use the model on real tweets from Twitter API. And compare to price of the stock.
* Use more ML models.

## Sources
* Papers: 
    * https://arxiv.org/pdf/1812.04199.pdf  
    * https://arxiv.org/pdf/1607.01958.pdf  
    * https://journalofbigdata.springeropen.com/articles/10.1186/s40537-017-0111-6
    * https://link.springer.com/article/10.1007/s42979-020-0076-y
* Tutorials/explanations: 
    * https://medium.com/@gabriel.mayers/sentiment-analysis-from-tweets-using-recurrent-neural-networks-ebf6c202b9d5
    * https://www.youtube.com/watch?v=LHXXI4-IEns
    * https://www.youtube.com/watch?v=8HyCNIVRbSU
    * https://www.youtube.com/watch?v=6niqTuYFZLQ
* API Docs: 
    * Twitter API: https://developer.twitter.com/en/docs
    * Yahoo finance python package: https://pypi.org/project/yfinance/
  