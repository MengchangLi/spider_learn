import requests
from fake_useragent import UserAgent
import random
from bs4 import BeautifulSoup
import time
import chardet

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/hongloumeng.html'
    ua = UserAgent()
    headers = {'User-Agent':ua.firefox}
    print(headers)

    # 拿到首页数据
    response = requests.get(url=url, headers=headers)
    response.encoding = chardet.detect(response.content)
    page_text = response.text
    print(response.encoding)

    # 解析章节标题及对应url
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open("./hongloumeng.txt","w",encoding="utf-8")
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+ li.a['href']
        detail_page = requests.get(detail_url, headers=headers)
        detail_page.encoding = chardet.detect(detail_page.content)
        detail_text = detail_page.text

        detail_soup = BeautifulSoup(detail_text, 'lxml')
        detail_content = detail_soup.find("div", attrs="chapter_content").text

        fp.write(title+':'+detail_content+'\n')
        print(title+'获取成功')
        time.sleep(random.randint(1, 2))