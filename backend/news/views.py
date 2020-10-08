# -*-coding:utf-8-*-


from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import NewsData, Pics, Token
from .serializers import NewsDataSerializer, NewsDetailSerializer

import random
import string
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import ConfigParser
config = ConfigParser.ConfigParser()
config.read('./config.ini')
admin_password = config.get('admin','password')


def token_update(func):
  def warpper(*args,**kwargs):
    new_token = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    if not Token.objects.filter(id=1):
        Token(token=new_token).save()

    old_token = Token.objects.get(id=1)
    if str(old_token.date) != time.strftime("%Y-%m-%d", time.localtime()):
        old_token.token = new_token
        old_token.save()
    return func(*args,**kwargs)
  return warpper


def token_check(func):
  def warpper(*args,**kwargs):
    data = args[1].data
    token = data.get('token')
    # 校验token
    if not token or not Token.objects.filter(token=token):
        return Response({"msg":"no token or token out of date."}, HTTP_400_BAD_REQUEST)
    return func(*args,**kwargs)
  return warpper


class NewsDataView(viewsets.ModelViewSet):
    queryset = NewsData.objects.all()
    serializer_class = NewsDataSerializer
    pagination_class = LimitOffsetPagination
    filter_fields = ('id', 'title', 'headline')


class NewsDetailView(viewsets.ModelViewSet):
    queryset = NewsData.objects.all()
    serializer_class = NewsDetailSerializer
    filter_fields = ('id',)


class SubmitNewsView(APIView):
    @token_update
    @token_check
    def post(self, request):
        data = request.data
        id = data.get('id')

        data['cover'] = re.search(r'<img src="([^"]*)', data.get('content'))
        if not data['cover']:
            data['cover'] = "http://47.103.209.239/api/pic/?code=ETfHx14vX3"
        else:
            data['cover'] = data['cover'].group(1)

        news_data = None
        if not id or id <= 0 or not NewsData.objects.filter(id=id):
            news_data = NewsData()
        else:
            news_data = NewsData.objects.get(id=id)

        news_data.__dict__.update(**data)
        news_data.save()
        return Response({}, HTTP_200_OK)


class DeleteNewsView(APIView):
    @token_update
    @token_check
    def post(self, request):
        data = request.data
        id = data.get('id')

        if not NewsData.objects.filter(id=id):
            return Response({}, HTTP_400_BAD_REQUEST)

        NewsData.objects.get(id=id).delete()
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


# 获取token
class TokenView(APIView):
    @token_update
    def get(self, request):
        data = request.query_params.dict()
        password = data.get('password')
        if not password or password != admin_password:
            return Response({}, HTTP_400_BAD_REQUEST)
        return Response({'token':Token.objects.get(id=1).token}, HTTP_200_OK)


# 前端入口
def index(request):
    return render(request, 'index.html')
