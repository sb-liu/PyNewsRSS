import feedparser
import requests_futures

if __name__ == "__main__":

    # Washington Post: http://feeds.washingtonpost.com/rss/politics
    # NYT: http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml
    # CNN: http://rss.cnn.com/rss/cnn_allpolitics.rss
    # ABC: https://abcnews.go.com/abcnews/politicsheadlines
    # Fox: http://feeds.foxnews.com/foxnews/politics

    source_list = ['http://feeds.washingtonpost.com/rss/politics',
                   'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml' ,
                   'http://rss.cnn.com/rss/cnn_allpolitics.rss',
                   'https://abcnews.go.com/abcnews/politicsheadlines',
                   'http://feeds.foxnews.com/foxnews/politics'
                   ]

    # Each entry has the following common properties:
    # 'title', 'title_detail', 'summary', 'summary_detail', 'links',

    # go through each news outlet
    for source in source_list:
        # get the parsed RSS feed
        d = feedparser.parse(source)
        # extract each head line
        a = d['entries']
        for title in a:
            print(title['title'])







