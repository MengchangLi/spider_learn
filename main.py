### 第一个python爬虫
import urllib.request as request

from fake_useragent import UserAgent

# 测试网站
url = 'https://acg.is/d/10905-encrypto'

# 重构请求头
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}

# 使用fake_useragnet获取随机UA
ua = UserAgent()
headers = {'User-Agent': ua.random}

# 伪装请求头
req = request.Request(url=url, headers=headers)

# 向url发出请求，获取响应对象
response = request.urlopen(req)
print(response)

# 解析出html
html = response.read().decode('utf-8')
with open("cont2.txt", 'w', encoding='utf-8') as f:
    f.write(html)
