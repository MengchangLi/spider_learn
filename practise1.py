from urllib import parse
from urllib import request
from fake_useragent import UserAgent

def get_url(word):
    url = "https://www.baidu.com/s?{}"
    word = parse.urlencode({"wd":word})
    url.format(word)
    return url

def request_url(url, filename):
    ua = UserAgent()
    header = {'User-Agent': ua.firefox}
    req = request.Request(url=url, headers=header)
    res = request.urlopen(req)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(res.read().decode('utf-8'))

if __name__ == '__main__':
    word = input(' 请输入搜索内容')
    url = get_url(word)
    request_url(url, './test.html')
