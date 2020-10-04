from rest_framework import serializers
from .models import NewsData

class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        exclude = []