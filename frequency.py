import sys
import json

def hw():
#    print 'Hello, world!'
    tweet_file = open(sys.argv[1])
    tweet_count=0
    all_words=0
    related={}
#    print "begin tweet_lines"
    for line in tweet_file:
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
#      print repr(tweet['text'])
#      print repr(tweet_text)

      # Walk all words in tweet
      for word in words:
          all_words += 1
          # Store or increment each word
          if related.get(word) :
              related[word] += 1
#              print "incrementing ",word
          else:
#              print "initial ",word
              related[word]=1

#      print "next tweet_lines"

    # Format output
    for rel in related.items():
        term,term_count=rel
#        print "word %s count %d %1.2f" % ( term,term_count,float(1/3) )
#        print rel[0],rel[1],"/", all_words, "{:1.8f}".format( float(term_count)/float(all_words) )
        print "%s %f" % ( term,float(term_count)/all_words )

#    print "---",all_words
#      print "Tweet number ",tweet_count," scored ", total, tweet_text
#      print related.items()
#      print tweet_count, total
#      print  total

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw()
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
