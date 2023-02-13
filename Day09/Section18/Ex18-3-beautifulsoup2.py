import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
response = requests.get(url, params=None)
html = response.text
print(html)
