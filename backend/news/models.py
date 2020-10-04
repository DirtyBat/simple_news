# -*- coding: utf-8 -*-

from django.db import models

class NewsData(models.Model):
    # 新闻id
    id = models.AutoField(primary_key=True)
    # 新闻标题
    title = models.CharField(max_length=80, default="")
    # 新闻主要内容，可能要存图片的base64，所以开大一点
    text = models.CharField(max_length=300000, default="")
    # 创建日期
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Pics(models.Model):
    # 图片id
    id = models.AutoField(primary_key=True)
    # 图片
    pic = models.ImageField(upload_to="./pics/%Y-%m-%d")