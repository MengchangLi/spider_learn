from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='./chromedriver')
brow = webdriver.Chrome(service=s)

