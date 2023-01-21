# 网站请求方式改变
import requests
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool
from lxml import etree
import random

if __name__ == '__main__':
    # 对url进行请求，解析出视频详情页的url和视频名称
    cat_url = 'https://www.pearvideo.com/category_1'
    headers = {'User-Agent':UserAgent().browsers[random.randint(0, 5)]}
    response = requests.get(url=cat_url, headers=headers)
    tree = etree.HTML(response.text)

    li_list = tree.xpath('//div[@class="category-top"]//li[@class="categoryem "]')
    print(li_list)
    video_url_list = list()
    for li in li_list:
        content_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        title = li.xpath('./div/a/div[2]/text()')[0]
        print(content_url, title)
        detail_page = requests.get(url=content_url, headers=headers).text

        params = {
            'contId': 1176688
        }
        response = video_json = requests.get(url='https://www.pearvideo.com/videoStatus.jsp', headers=headers, params=params)
        print(response.json())
        # video_url_list.append()
    # content_url = 'https://www.pearvideo.com/' + tree.xpath('/html/body/div[2]/div[1]/div/ul/li[1]/div/a/@href')[0]
    # title = tree.xpath('/html/body/div[2]/div[1]/div/ul/li[1]/div/a/div[2]/text()')[0]
    # print(content_url, title)

    print(video_url_list)