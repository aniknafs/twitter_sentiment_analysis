import sys
import json

def tweet_sentiment(sent_file, tweet_file):
    tweets = [] 
    i = 0
    for line in tweet_file:
        tweets.append(json.loads(line))
        
    tweet_texts = []
    for i in range(len(tweets)):
        if(tweets[i].has_key('text')):
            tweet_texts.append(tweets[i]["text"].encode('utf-8'))
        else:  tweet_texts.append('')
        
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    sum = []
    for i in range(len(tweets)):
        tempSum = 0   
        words = tweet_texts[i].split()
        for word in words:
            s = scores.get(word)
            if(s != None): tempSum += s
        sum.append(tempSum)
        
    return sum, tweets     
    
def printState(tweet):
    if (tweet.has_key('place')):
            if(tweet['place'] != None):
                country = tweet['place']['country_code'] 
                if(country != None):
                    if(country == 'US'):
                        return tweet['place']['full_name']
    if (tweet.has_key('user')):
            if(tweet['user'].has_key('location')):
                    s = tweet['user']['location'].encode('utf-8').split(",")
                    if(len(s) == 2):
                        if len(s[1].split()[0]) == 2: 
                            return s[1].split()[0]


def main():
#    sent_file = open("AFINN-111.txt")
#    tweet_file = open("output-1000.txt")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ret = tweet_sentiment(sent_file, tweet_file)
    scores = ret[0]
    tweets = ret[1]

    sorted(scores)
    state = None
    i = 0
    while state == None and i < len(scores):   
        state = printState(tweets[scores[i]])
        i = i + 1
    print state
    
    
if __name__ == '__main__':
    main()
        