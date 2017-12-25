# -*-coding:utf-8-*-
from django.http import HttpResponse
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin


#禁止偶数IP访问
# class BlockIP(MiddlewareMixin):
#     def is_block_ip(self,ip):
#         return int(ip[-1]) % 2 == 0
#
#     def process_request(self,request):
#         ip = request.META['REMOTE_ADDR']
#         if self.is_block_ip(ip):
#             return HttpResponse('不欢迎你')

#使用Redis缓存
# def page_cache(timeout):
#     def wrap1(view_func):
#         def wrap2(request, *args, **kwargs):
#             key = 'page-%s' % request.get_full_path()
#             response = cache.get(key)
#             if response is None:
#                 print('exec view_func')
#                 response = view_func(request, *args, **kwargs)
#                 cache.set(key, response, timeout)
#             return response
#         return wrap2
#     return wrap1



