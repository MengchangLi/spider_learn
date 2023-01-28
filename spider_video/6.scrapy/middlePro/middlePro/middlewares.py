# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from fake_useragent import UserAgent

# 下载中间件重写
class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    ua = UserAgent()
    @classmethod
    # 拦截请求
    def process_request(self, request, spider):
        # 修改UA
        request.headers['UserAgent'] = self.ua.random

        return None

    # 拦截响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 拦截异常
    def process_exception(self, request, exception, spider):
        # 代理ip，通常写在异常中
        # 一般采用代理池，并判断请求类型
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://ip:port'
        else:
            request.meta['proxy'] = 'https://ip:port'

        # 修正后的对象再次请求
        return request