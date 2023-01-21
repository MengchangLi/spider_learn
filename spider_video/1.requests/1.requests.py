import requests

if __name__ == '__main__':
    # url
    url = 'https://www.baidu.com/'

    # send request
    res = requests.get(url=url)

    # get data in string
    page_text = res.text
    print(page_text)

    # save data
    with open('results/baidu.html', 'w', encoding='utf-8') as f:
        f.write(page_text)