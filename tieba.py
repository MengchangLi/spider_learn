from urllib import parse
from urllib import request
from ua_info import ua_list
import random
import time

class TiebaSpider():

    def __init__(self):
        self.url = "http://tieba.baidu.com/f?{}"

    # 形成url
    def form_url(self, kw, ie, pn):
        parm = {"kw": kw, "ie": ie, "pn": pn}
        parm = parse.urlencode(parm)
        url = self.url.format(parm)

    # 获取html文件
    def get_html(self):
        req = request.Request(url=self.url, headers={"User-Agent": random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 保存html文件
    def save_html(self, html, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def run(self):
        kw = input("请输入贴吧名：")
        ie = 'utf-8'
        begin = int(input('请输入起始页：'))
        end = int(input('请输入结束页：'))
        for page in range(begin, end+1):
            page=(page-1)*50
            self.form_url(kw, 'utf-8', page)
            html=self.get_html()
            self.save_html(html, './tieba/'+str(kw)+'_'+str(page)+'.html')
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider=TiebaSpider()
    spider.run()