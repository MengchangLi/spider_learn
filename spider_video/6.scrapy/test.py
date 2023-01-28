import requests

# random ua
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'UserAgent': ua.random}
print(headers)

print('/saf/asdf/asfd/'.split('/')[-2])
