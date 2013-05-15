twitter_sentiment_analysis
==========================
Sentiment analysis of the tweets 

The module tweet_analysis.py receives a term, an end date, a start date, and a number. It will then searches all the tweets containing the term which are published on or after the start date but before the end date. Due to the large number of tweets, you need to let the module know how many pages of tweets it should actually look for. Each page returned by Twitter search API returns about 15 tweets. 
The module will then do a sentiment analysis by comparing each term in the retrieved tweets with a list of pre-computed sentiment scores (stored in a file named AFINN-111.txt). More information about the sentiment scores can be obtained from AFINN-README.txt.  
==========================
How to execute the module

> python tweet_analysis.py [term] [yyyy-mm-dd] [yyyy-mm-dd] [number of tweet pages]

e.g. 
> python tweet_analysis.py 'google' '2013-05-15' '2013-05-14' 10