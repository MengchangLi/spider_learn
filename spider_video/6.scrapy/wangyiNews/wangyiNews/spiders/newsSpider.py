import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = 'newsSpider'
    # allowed_domains = ['news.163.com']
    start_urls = ['https://news.163.com/']

    def parse(self, response):

