# -*-coding:utf-8-*-


from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import NewsData, Pics
from .serializers import NewsDataSerializer

import random
import string
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class NewsDataView(viewsets.ModelViewSet):
    queryset = NewsData.objects.all()
    serializer_class = NewsDataSerializer
    filter_fields = ('id', 'title','headline')


class SubmitNewsView(APIView):
    def post(self, request):
        data = request.data
        title = data.get('title')
        summary = data.get('summary')
        headline = data.get('headline')
        content = data.get('content')
        cover = re.search(r'<img src="([^"]*)',content)
        
        if not cover:
            cover = "http://47.103.209.239/api/pic/?code=ETfHx14vX3"
        else:
            cover = cover.group(1)

        NewsData(title=title,
                 summary=summary,
                 cover=cover,
                 headline=headline,
                 content=content).save()
        
        return Response({}, HTTP_200_OK)


class SubmitPicView(APIView):
    def post(self, request):
        data = request.data
        random_string = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        pic = Pics(code=random_string,pic=data.get('pic'))
        pic.save()
        return Response({"code":random_string}, HTTP_200_OK)


    def get(self, request):
        data = request.query_params.dict()
        code = data.get('code')
        if not code or not Pics.objects.filter(code=code):
            return Response({}, HTTP_400_BAD_REQUEST)
        
        pic_path = str(Pics.objects.get(code=code).pic)
        with open(pic_path, 'rb') as f:
            pic_data = f.read()
        return HttpResponse(pic_data, content_type="image/png")


# 前端入口
def index(request):
    return render(request, 'index.html')
