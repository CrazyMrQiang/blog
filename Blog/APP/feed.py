# -*-coding:utf-8-*-
from django.contrib.syndication.views import Feed

from APP.models import Post


class AllPostRssFeed(Feed):
    title = '王小强的博客'
    link = '/'
    description = '我有酒，你有故事吗？'

    def items(self):
        return Post.objects.all()

    def item_title(self,item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self,item):
        return item.body