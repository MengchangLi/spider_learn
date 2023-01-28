import scrapy
from yande_re_db.items import YandeReDbItem
class PublicpicSpider(scrapy.Spider):
    name = 'publicPic'
    # allowed_domains = ['beats0.github.io']
    start_urls = ['https://beats0.github.io/scripter/yande.re_db/r.json']
    url_title = 'https://steamuserimages-a.akamaihd.net/ugc/'

    def parse(self, response):
        json = response.json()
        for j in json['pics']:
            # pic = response.content()
            pic_name = j + '.jpeg'
            pic_url = self.url_title + j
            print(pic_url)
            item = YandeReDbItem()
            item['src'] = pic_url

            yield item
            #
            # yield scrapy.Request(url, callback=self.parse_pic, meta={'item':item})
    #
    # def parse_pic(self, response):
    #     print('yes')
    #     item = response.meta['item']
    #     item['pic_data'] = response.body
    #     yield item



