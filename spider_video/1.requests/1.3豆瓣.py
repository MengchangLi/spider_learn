import requests
import json
from fake_useragent import UserAgent
import random

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '6',
        'interval_id':'100:90',
        'action':'',
        'start':'0',
        'limit':'20'
    }
    ua = UserAgent()
    headers = {'User-Agent':ua.browsers[random.randint(0,5)]}

    response = requests.get(url=url,params=params,headers=headers)
    list_data = response.json()

    with open('results/douban.json', 'w', encoding='utf-8') as f:
        json.dump(list_data,f,ensure_ascii=False)