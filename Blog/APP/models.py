# -*-coding:utf-8-*-

from django.contrib.auth.models import User
from django.db import models

#分类
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#标签云
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#文章
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #摘要
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    Tags = models.ManyToManyField(Tag,blank=True)
    #User 是Django 为我们写好的用户模型
    author = models.ForeignKey(User)
    #阅读量
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])