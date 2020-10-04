# -*-coding:utf-8-*-

from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import NewsData
from .serializers import NewsDataSerializer


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class NewsDataView(viewsets.ModelViewSet):
    queryset = NewsData.objects.all()
    serializer_class = NewsDataSerializer
    filter_fields = ('id', 'title')


class SubmitNewsView(APIView):
    def post(self, request):
        data = request.data
        # todo


# 前端入口
def index(request):
    return render(request, 'index.html')
