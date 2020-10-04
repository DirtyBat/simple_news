# -*-coding:utf-8-*-


from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import NewsData, Pics
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


class SubmitPicView(APIView):
    def post(self, request):
        data = request.data
        pic = Pics(pic=data.get('pic'))
        pic.save()
        return Response({"id":str(pic.id)}, HTTP_200_OK)


    def get(self, request):
        data = request.query_params.dict()
        id = data.get('id')
        if not id or not Pics.objects.get(id=id).pic:
            id = 1
        
        pic_path = str(Pics.objects.get(id=id).pic)
        with open(pic_path, 'rb') as f:
            pic_data = f.read()
        return HttpResponse(pic_data, content_type="image/png")


# 前端入口
def index(request):
    return render(request, 'index.html')
