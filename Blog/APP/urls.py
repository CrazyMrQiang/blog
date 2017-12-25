# -*-coding:utf-8-*-
from django.conf.urls import url

from APP import views

from django.views.decorators.cache import cache_page


urlpatterns = [

    # url(r"index/",cache_page(60*15)(views.IndexView.as_view()),name='index'),
    url(r"index/",views.IndexView.as_view(),name='index'),
    url(r'post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
    url(r'tags/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    url(r'search/',views.search,name='search'),


]