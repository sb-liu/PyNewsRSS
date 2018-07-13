from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from tag import gen_tags
from nltk.corpus import stopwords

# Create your views here.
def index(request):
    return render(request, 'generator/index.html')

def tag_response(request):
    # setting the stop words
    stops = set(stopwords.words('english'))

    # Removes titles such as WATCH: BREAKING NEWS
    stops.add('watch')

    # first tokenize the text
    source_list = ['http://feeds.washingtonpost.com/rss/politics',
                'http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml',
                'https://abcnews.go.com/abcnews/politicsheadlines',
                ]
    list_tags = gen_tags(source_list, stops)
    html_content = ""
    for tag in list_tags:
        line = tag[0] + ": " + str(tag[1]) + "\n"
        html_content += line
    return render(request, 'generator/index.html', context={'a':html_content})