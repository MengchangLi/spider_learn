from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from lxml import etree

# 实例化一个浏览器对象
s = Service(executable_path='./chromedriver')
brow = webdriver.Chrome(service=s)

brow.get('https://www.pearvideo.com/video_1176688')

time.sleep(2)

page_text = brow.page_source
tree = etree.HTML(page_text)
print(tree.xpath('/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/video/@src'))