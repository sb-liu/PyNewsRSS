from __future__ import division
import feedparser
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter


# 1. Create a freq list from the article summary
# 2. Rank the title of the article based on the freq list in step 1
# 3. Create the hash tags based on given ratio (hashtag/title)




# setting the stop words
stops = set(stopwords.words('english'))

# Removes titles such as WATCH: BREAKING NEWS
stops.add('WATCH')

# first tokenize the text
source_list = ['http://feeds.washingtonpost.com/rss/politics',
               'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
               'https://abcnews.go.com/abcnews/politicsheadlines',
               ]

# Each entry has the following common properties:
# 'title', 'title_detail', 'summary', 'summary_detail', 'links',

headlines = []
# used for stemming
ps = PorterStemmer()
# our counter for word frequency
ct = Counter()
word_tokenize = RegexpTokenizer(r'\w+')
# go through each news outlet
for source in source_list:
    # get the parsed RSS feed
    d = feedparser.parse(source)
    # extract each head line
    a = d['entries']
    for title in a:
        # removes punctuation and tokenizes the word
        words = word_tokenize.tokenize(title['title'])
        # removes stop words
        filtered_words = [word for word in words if word not in stops]
        # stem the words and add them to the counter
        for fw in filtered_words:
            #ct[ps.stem(fw)] += 1
            ct[fw] += 1
        #print(filtered_words)

#print(ct)
