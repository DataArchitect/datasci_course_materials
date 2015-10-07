import sys
import json

def hw():
#    print 'Hello, world!'
    sent_file = open(sys.argv[1])
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

#    print scores.items() # Print every (term, score) pair in the dictionary

    tweet_file = open(sys.argv[2])
    tweet_count=0
    for line in tweet_file:
      score=0
      total=0
      tweet=json.loads(line)
#      print tweet.viewkeys()
      tweet_text=tweet.get('text')
      if tweet_text != None: 
        if len(tweet_text) == 0:
            continue
        # We know it's unicode
        tweet_text=tweet_text.encode('utf-8')
#        print "unicode ",tweet_text
#        print "splitted"
        # convert bytes to chars
#        tweet_text=tweet_text.decode('utf-8',errors='ignore')
#        pass
      else:
        continue

      # Process tweet with text
      words=tweet_text.split()
      tweet_count+=1
      related={}
#      print repr(tweet['text'])
#      print repr(tweet_text)

      # has sentiment?
      for term in scores.keys():
#        print "checking ",term," in ",tweet_text
        if tweet_text.find(term) != -1:
            score=scores[term]
#            print term," found score of ",score
            # Walk all words in tweet
            for word in words:
                # skip already found and sentiments 
                if related.get(word) or scores.get(word):
                    continue
                else:
#                    print "checking ",word
                    related[word]=score
        total+=score
      # Format output
      for rel in related.items():
        print rel[0],rel[1]

#      print "Tweet number ",tweet_count," scored ", total, tweet_text
#      print related.items()
#      print tweet_count, total
#      print  total

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
