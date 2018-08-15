from django.shortcuts import render
from . news_api import NewsApi, NewsApiEverything

# Create your views here.
def index(request):
    query = request.GET.get('search')
    if query:
        news_obj = NewsApi(query)
    else:
        news_obj = NewsApi('World')
    discription = news_obj.get_description()
    url = news_obj.get_url()
    images = news_obj.get_images()
    title = news_obj.get_title()
    mylist = zip(title, discription, images, url)
    slide_list = zip(images[:8], title[:8], url[:8])
    context = {
        'mylist': mylist,
        'slide_list': slide_list,
    }
    return render(request, 'home.html',context)

def cricket_news(request):
    sources = 'espn-cric-info, fox-sports'
    news_obj = NewsApiEverything('cricket', sources)
    discription = news_obj.get_description()
    url = news_obj.get_url()
    images = news_obj.get_images()
    title = news_obj.get_title()
    mylist = zip(title, discription, images, url)
    context = {
        'mylist': mylist,
    }
    return render(request,'cricket.html',context)
