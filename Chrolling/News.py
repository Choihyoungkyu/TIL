#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup as bs
import requests

url = 'https://search.naver.com/search.naver?where=news&query=커리'

response = requests.get(url)
html_text = response.text

soup = bs(html_text, 'html.parser')

# print(soup.select_one('a.news_tit').get_text())

titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    link = i.get_attribute_list('href')
    print(f'{title}\n{link}\n')


# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = bs(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))