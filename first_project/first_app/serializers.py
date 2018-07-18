from . models import Topic, Webpage, AccessRecord
from rest_framework import serializers

class TopicSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('top_name')

class WebpageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Webpage
        fields = ('topic', 'name', 'url')

class AccessRecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessRecord
        fields = ('name', 'date')
