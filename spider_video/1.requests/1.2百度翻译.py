import requests
import fake_useragent
import json

if __name__=='__main__':
    #1. 指定url和参数
    url = 'https://fanyi.baidu.com/sug'
    kw = input("请输入需要翻译的单词")
    params = {'kw':kw}

    # 2. UA伪装
    ua = fake_useragent.UserAgent()
    headers = {'User-Agent':ua.firefox}

    # 3. 发送请求
    response = requests.post(url=url,params=params,headers=headers)

    # 4. 解析请求
    response_json = response.json()

    # 5. 持久化存储
    filename = kw + '.json'
    with open('./'+filename,'w',encoding='utf-8') as f:
        json.dump(response_json, f, ensure_ascii=False)
