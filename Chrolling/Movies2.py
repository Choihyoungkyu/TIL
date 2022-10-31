import requests
from bs4 import BeautifulSoup as bs
import json

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

response = requests.get(url)
html_text = response.text

soup = bs(html_text, 'html.parser')
# print(soup)
# print(soup.select_one('a.news_tit').get_text())

titles = soup.select('div.tit3 > a')
# print(titles)

# for i in range(len(titles)):
for i in range(10):
    title = titles[i].get_text()
    link = 'https://movie.naver.com'
    link += titles[i].get_attribute_list('href')[0]
    print(f'\n{i+1}위 {title}\n{link}')