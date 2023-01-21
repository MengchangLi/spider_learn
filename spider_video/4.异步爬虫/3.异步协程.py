import time
import asyncio

async def request(url):
    print('正在下载', url)
    time.sleep(2)
    print("下载完成", url)

urls = [
    "www.baidu.com"
    "www.sougou.com"
    "www.google.com"
]

tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

