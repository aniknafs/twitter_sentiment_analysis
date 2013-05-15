import urllib
import json
import sys 

def retreive_tweets(term, date_until, date_from, page_num):
    response = []
    pyresponse = []
    for i in range(page_num):
        response.append(urllib.urlopen("http://search.twitter.com/search.json?q="+term+"%20lang%3Aen%20until%3A"+date_until+"%20since%3A"+date_from+"&page="+ str(i+1)))
        pyresponse.append(json.load(response[i]))
    return pyresponse

def sentiment_analysis(tweet_pages):    
    sent_file = open("AFINN-111.txt")
    
#    extracts tweets out of tweet pages
    tweets = []
    for i in range(len(tweet_pages)):
        for j in range(len(tweet_pages[i]['results'])):
            tweets.append(tweet_pages[i]['results'][j])
    print str(len(tweets)) + ' tweets were analyzed.'
    
#    extracts tweets' texts
    tweet_texts = []
    for i in range(len(tweets)):    
        if(tweets[i].has_key('text')): 
            tweet_texts.append(tweets[i]["text"].encode('utf-8'))
        
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
        
    tweet_score = []
    for i in range(len(tweets)):
        tempSum = 0   
        words = tweet_texts[i].split()
        for word in words:
            s = scores.get(word)
            if(s != None): tempSum += s
        tweet_score.append(tempSum)
        
    return float(sum(tweet_score))/len(tweets)
                                    
def main():
    term = sys.argv[1]
    date_until = sys.argv[2] # yyyy-mm-dd and are assumed to be from/to 00:00 UTC.
    date_from = sys.argv[3]
    page_num = int(sys.argv[4])
    
#    retrieves the first 'page_num' pages of the tweets mentioning 'term' between 'date_from' to 'date_until'
    tweets = retreive_tweets(term, date_until, date_from, page_num) 
    
#    performs the sentiment analysis on the retreived tweets
    avg_score = sentiment_analysis(tweets)
    
    print 'Average sentiment score of tweets containing the term: %s from %s until %s is: %.2f' % (term, date_from, date_until, avg_score)
    
if __name__ == '__main__':
    main()
