import requests
from fake_useragent import UserAgent
from lxml import etree
import chardet

if __name__ == '__main__':
    url = "https://su.58.com/ershoufang/p{}"
    headers = {'User-Agent':UserAgent().random}

    url += '1'

    page = requests.get(url=url, headers=headers)
    print(page.encoding)
    page.encoding = chardet.detect(page.content)['encoding']
    print(page.encoding)
    page_text = page.text

    tree = etree.HTML(page_text)
    title_list = tree.xpath('//h3[@class="property-content-title-name"]/text()')
    print(title_list)