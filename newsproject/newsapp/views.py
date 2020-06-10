# importing api
from django.shortcuts import render

from newsapi import NewsApiClient


# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='b8289c01e91243f598cc8c98f00f90e6')
    top = newsapi.get_everything(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})
