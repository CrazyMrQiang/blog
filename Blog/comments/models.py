from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
#装饰器用于兼容python2
@python_2_unicode_compatible
class Comment(models.Model):   #评论专区
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    url = models.URLField(blank=True)
    text = models.TextField()
    #auto_now_add 评论保存到数据库是 自动把created_time指定为当前时间
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('APP.Post')

    def __str__(self):
        return self.text[:20]
