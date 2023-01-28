import scrapy


class BossspiderSpider(scrapy.Spider):
    name = 'bossSpider'
    # allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/wapi/zpgeek/search/joblist.json?query=python&city=100010000&page=1&pageSize=30']
    url_model = 'https://www.zhipin.com/job_detail/%s.html'

    def parse(self, response):
        json = response.json()
        print(json)
        for j in json['zpData']['jobList']:
            new_url = self.url_model.format(j['encryptBossId'])
            yield scrapy.Request(url=new_url, callback=self.parse_detail)

    def parse_detail(self, response):
        job_detail = response.xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/text()')
        print(job_detail)