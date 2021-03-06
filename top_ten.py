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
      tweet_entities=tweet.get('entities')
      if not (tweet_entities) :
        continue

      tweet_hashtags=tweet_entities.get('hashtags')
#      print tweet_entities.viewkeys()
#      print "tags:",tweet_hashtags
      for tag_obj in tweet_hashtags:
          tag_text=tag_obj['text']
          if not (tag_text) :
            continue
          else:
            # We know it's unicode
            word=tag_text.encode('utf-8')

#          print "tag_obj",word
#        print "unicode ",tweet_text
#        print "splitted"
        # convert bytes to chars
#        tweet_text=tweet_text.decode('utf-8',errors='ignore')
#        pass

          tweet_count+=1
#      print repr(tweet['text'])
#      print repr(tweet_text)

          # tags are single words?
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
    display_count=0
    ten_array= ( sorted( related.values(), reverse=True ) )[0:9]
    for val in ten_array:
        for rel in related.items():
            # Break here or we overrun
            if display_count>9 :
                break
            term,term_count=rel
            if term_count == val:
                print term,term_count
                display_count+=1
        
#            print "rejecting low"

#        print "word %s count %d %1.2f" % ( term,term_count,float(1/3) )
#        print rel[0],rel[1],"/", all_words, "{:1.8f}".format( float(term_count)/float(all_words) )
#        print "%s %f" % ( term,float(term_count)/all_words )

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
