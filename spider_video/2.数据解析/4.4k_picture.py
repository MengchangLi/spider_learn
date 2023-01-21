import requests
from fake_useragent import UserAgent
import chardet
from lxml import etree
import os

if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {'User-Agent':UserAgent().random}

    response = requests.get(url=url, headers=headers)
    response.encoding = chardet.detect(response.content)['encoding']
    page_text = response.text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    # print(li_list)

    for li in li_list:
        pic_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
        pic_res = requests.get(url=pic_src, headers=headers)
        if not os.path.exists("./4k_pic"):
            os.mkdir("./4k_pic")
        filename = os.path.join('./4k_pic', li.xpath('./a/b/text()')[0]+'.jpg')
        with open(filename,'wb') as f:
            f.write(pic_res.content)
            print(filename+"下载成功")