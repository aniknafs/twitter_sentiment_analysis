import sys
import json
 
def lines(fp):
    print str(len(fp.readlines()))

def tweet_sentiment(sent_file, tweet_file):
    tweets = [] # Stores the tweets
    for line in tweet_file:
        tweets.append(json.loads(line))
    
    tweet_texts = [] # Stores the text part of the tweets
    for i in range(len(tweets)):
        tweet_texts.append(tweets[i]["text"].encode('utf-8'))
        
    scores = {} # Read the sentiments file and copy it into a dictionary
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    outsiders = {} # Includes those words that are not in the sentiments file
    sum = [] # Stores the sum of sentiment scores for each tweet
    for i in range(len(tweets)):
        tempSum = 0   
        words = tweet_texts[i].split()
        for word in words:
            s = scores.get(word)
            if(s != None): tempSum += s
        sum.append(tempSum)
        for word in words: 
            if(scores.get(word) == None):
                if(outsiders.get(word) == None):
                    outsiders[word] = sum[i]
                else: outsiders[word] = outsiders[word] + sum[i]
            
#    scores.update(outsiders)        
    for k, v in outsiders.iteritems(): # Print out each pair from the dict
        print '%s %d' % (k,v)

def main():
#    sent_file = open("AFINN-111.txt")
#    tweet_file = open("output.txt")
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    tweet_sentiment(sent_file, tweet_file)

if __name__ == '__main__':
    main()
