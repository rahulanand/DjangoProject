# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . news_api import NewsApi

# Create your views here.
def index(request):
    news_obj = NewsApi(None)
    discription = news_obj.get_description()
    url = news_obj.get_url()
    images = news_obj.get_images()
    title = news_obj.get_title()
    length = list(range(len(title)))
    return render(request, 'home.html',context=({'discriptions': discription, 'urls':url, 'images':images, 'titles': title, 'length': length}))
