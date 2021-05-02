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