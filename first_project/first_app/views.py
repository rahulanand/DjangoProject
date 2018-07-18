from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from rest_framework import viewsets
from . serializers import TopicSerializers, WebpageSerializers, AccessRecordSerializers
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'first_app/index.html', context=date_dict)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers

class WebpageViewSet(viewsets.ModelViewSet):
    queryset = Webpage.objects.all()
    serializer_class = WebpageSerializers

class AccessViewSet(viewsets.ModelViewSet):
    queryset = AccessRecord.objects.all()
    serializer_class = AccessRecordSerializers


