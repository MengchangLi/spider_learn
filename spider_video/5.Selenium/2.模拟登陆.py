import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random

s = Service(executable_path='./chromedriver')
brow = webdriver.Chrome(service=s)

brow.get('https://qzone.qq.com/')
time.sleep(2)

brow.switch_to.frame('login_frame')
a_tag = brow.find_element(by=selenium.webdriver.common.by.By.ID, value='switcher_plogin')
a_tag.click()
time.sleep(0.5)

username_input = brow.find_element(by=selenium.webdriver.common.by.By.ID, value='u')
pass_input = brow.find_element(by=selenium.webdriver.common.by.By.ID, value='p')
username_input.send_keys('')
pass_input.send_keys('')
time.sleep(0.6)

btn_login = brow.find_element(by=selenium.webdriver.common.by.By.ID, value='login_button')
btn_login.click()

time.sleep(3)