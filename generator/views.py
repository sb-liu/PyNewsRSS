from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from tag import gen_tags
from nltk.corpus import stopwords
import json

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
    head_line_dict = dict()
    for tag in list_tags:
        head_line_dict[tag[0]] = str(tag[1])
    return render(request, 'generator/index.html',{'head_lines': head_line_dict})