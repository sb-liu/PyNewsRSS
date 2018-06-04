from __future__ import division
import feedparser
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
from urllib.request import ProxyHandler


# setting the stop words
stops = set(stopwords.words('english'))

# Removes titles such as WATCH: BREAKING NEWS
stops.add('watch')

# first tokenize the text
source_list = ['http://feeds.washingtonpost.com/rss/politics',
               'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
               'https://abcnews.go.com/abcnews/politicsheadlines',
               ]

# Each entry has the following common properties:
# 'title', 'title_detail', 'summary', 'summary_detail', 'links',

def gen_tags(rss, stops, proxy):
    # support for Proxy
    protocol = proxy.split("/")[0][:-1]
    our_proxy = ProxyHandler({protocol: proxy})
    headlines = []
    # used for stemming
    ps = PorterStemmer()
    # our counter for word frequency
    ct = Counter()
    ct2 = Counter()
    word_tokenize = RegexpTokenizer(r'\w+')
    # stores tokenized headlines
    list_titles = []
    # go through each news outlet
    for source in rss:
        # get the parsed RSS feed
        d = feedparser.parse(source,  handlers=[our_proxy])
        # extract each head line
        a = d['entries']
        for title in a:
            # removes punctuation and tokenizes the word
            words = word_tokenize.tokenize(title['title'])
            # removes stop words
            filtered_words = [word for word in words if (word.lower()) not in stops]
            list_titles.append(filtered_words)
            # stem the words and add them to the counter
            for fw in filtered_words:
                ct[ps.stem(fw)] += 1
                ct2[fw] += 1

    tags = dict(ct.most_common(20))
    processed_set = Counter()
    # go through each title and see if we can combine tags ie. #south #korea -> #South Korea
    is_prev_tag = False
    prev = ""
    for title in list_titles:
        for index in range(1, len(title)):
            if (title[index-1].lower() in tags) and (title[index].lower() in tags):
                combined = title[index-1] + " " + title[index]
                processed_set[combined] += 1
                is_prev_tag = True
            else:
                if (title[index-1].lower() in tags) and not is_prev_tag:
                    processed_set[title[index - 1]] += 1
                is_prev_tag = False

    return processed_set.most_common(5)




