from urllib import parse, request
import time
import random
from fake_useragent import UserAgent
import re
import csv

class MaoyanSpider():

    def __init__(self) -> None:
        self.url = 'https://www.maoyan.com/board/4?{}'

    def get_html(self, offset):
        self.url.format(parse.urlencode({'offset': offset}))
        ua = UserAgent()
        req = request.Request(url=self.url, headers={'User-Agent':ua.firefox})
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parse_html(html)

    def parse_html(self, html):
        re_dbs = '<div class="movie-item-info">.*?title="(.*？)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">上映时间：(.*?)</p>'
        regex = re.compile(re_dbs, re.S)
        r_list = regex.findall(html)
        print(type(r_list))
        print(r_list)
        self.save_html(r_list)

    def save_html(self, r_list):
        # with open('maoyan.csv', 'a', newline='', encoding='utf-8') as f:
        #     writer = csv.writer(f, dialect='excel')
        #     for r in r_list:
        pass

    def run(self):
        for offset in range(0, 10):
            self.get_html(offset*10)
            time.sleep(random.uniform(1,2))

if __name__ == '__main__':
    maoyan = MaoyanSpider()
    maoyan.run()

