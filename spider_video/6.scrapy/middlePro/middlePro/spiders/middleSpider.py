import scrapy


class MiddlespiderSpider(scrapy.Spider):
    name = 'middleSpider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
