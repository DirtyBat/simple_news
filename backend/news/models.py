# -*- coding: utf-8 -*-

from django.db import models

class NewsData(models.Model):
    # 新闻id
    id = models.AutoField(primary_key=True)
    # 新闻标题
    title = models.CharField(max_length=80, default="")
    # 新闻主要内容
    content = models.CharField(max_length=300000, default="")
    # 创建日期
    date = models.DateField(auto_now=True)
    # 是否是头条
    headline = models.BooleanField(default=False)
    # 分类
    types = models.CharField(max_length=100, default="")
    # 简介
    summary = models.CharField(max_length=2000, default="")
    # 封面图片,等待设置一个默认连接
    cover = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.title


class Pics(models.Model):
    # 图片code
    code = models.CharField(max_length=50,default="")
    # 图片
    pic = models.ImageField(upload_to="./pics/%Y-%m-%d")


class Token(models.Model):
    # token
    token = models.CharField(max_length=20,default="")
    # 创建日期
    date = models.DateField(auto_now=True)
