# -*-coding:utf-8-*-
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from APP.models import Post, Category, Tag
import markdown
from comments.forms import CommentForm


class IndexView(ListView,HttpRequest):
    model = Post
    template_name = 'APP/index.html'
    context_object_name = 'post_list'
    paginate_by = 3


#分类
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category = cate)

#归档
class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super().get_queryset().filter(created_time__year=year,created_time__month=month)

#标签云
class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(Tags=tag)

#详情页
class PostDetailView(DetailView):
    model = Post
    template_name = 'APP/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 重写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super().get(request,*args,**kwargs)
        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        # 重写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.nl2br',
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        # 重写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板
        context = super(PostDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({ 'form': form, 'comment_list': comment_list})
        return context

#简单的全文搜索
def search(request):
    sousuo = request.GET.get('sousuo')
    error_msg = ''
    if not sousuo:
        error_msg = '请输入关键词'
        return render(request,'APP/index.html',{'error_msg':error_msg})
    post_list = Post.objects.filter(Q(title__icontains=sousuo)|Q(body__icontains=sousuo))
    return render(request,'APP/index.html',{'error_msg':error_msg,'post_list':post_list})


