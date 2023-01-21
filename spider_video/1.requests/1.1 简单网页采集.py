import requests

if __name__ == '__main__':
    # 1.指定url
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    url = 'https://cn.bing.com/search?'
    #   处理参数
    q = input("请输入搜索值：")
    param = {'q':q}

    # 2.发送请求，获取响应
    response = requests.get(url=url, params=param)

    # 3.处理响应
    page_text = response.text

    # 4.持久化存储
    filename = q + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_text)