# -*-coding:utf-8-*-

from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

#将函数注册为模板标签
register = template.Library()

#最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

#归档模板标签
@register.simple_tag
def archives():
  return Post.objects.dates('created_time','month',order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

#标签云模板
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)