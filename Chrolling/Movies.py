import requests
from bs4 import BeautifulSoup as bs
import json

url = 'https://openapi.naver.com/v1/search/movie.json'
headers = {
    'Host': 'openapi.naver.com',
    'User-Agent': 'curl/7.49.1',
    'Accept': '*/*',
    'X-Naver-Client-Id' : 'Iub9il38FjlWAQnyLB_g',
    'X-Naver-Client-Secret': '1cJFxDfJmH',
}
params = {'query': '로맨스',
          'genre': '5'}
response = requests.get(url, headers=headers, params=params)
print(response.text)

jsonObject = json.loads(response.text)
# print(jsonObject.get("lastBuildDate"))