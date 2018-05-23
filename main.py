import feedparser
from rake_nltk import Rake

if __name__ == "__main__":

    # Washington Post: http://feeds.washingtonpost.com/rss/politics
    # NYT: http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml
    # CNN: http://rss.cnn.com/rss/cnn_allpolitics.rss
    # ABC: https://abcnews.go.com/abcnews/politicsheadlines
    # Fox: http://feeds.foxnews.com/foxnews/politics

    source_list = ['http://feeds.washingtonpost.com/rss/politics',
                   'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml' ,
                   'https://abcnews.go.com/abcnews/politicsheadlines',
                   ]

    # Each entry has the following common properties:
    # 'title', 'title_detail', 'summary', 'summary_detail', 'links',
    r = Rake()
    headlines = []
    # go through each news outlet
    for source in source_list:
        # get the parsed RSS feed
        d = feedparser.parse(source)
        # extract each head line
        a = d['entries']
        for title in a:
            #headlines.append(title['summary'])
            r.extract_keywords_from_text(title['summary'])
            print(r.get_ranked_phrases_with_scores()[0:3])
        headlines = []





