# -*-coding:utf-8-*-

import views
from django.conf.urls import url, include
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register('news_data', views.NewsDataView)
routers.register('news_detail', views.NewsDetailView)

urlpatterns = [
    url(r'^api/', include(routers.urls)),
    url(r'^api/submit_news', views.SubmitNewsView.as_view()),
    url(r'^api/pic', views.SubmitPicView.as_view()),
    url(r'^api/get_token', views.TokenView.as_view()),
    url(r'^.*?$', views.index),
]
