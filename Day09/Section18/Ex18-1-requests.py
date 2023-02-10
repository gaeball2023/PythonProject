'''
모듈 설치 requests
pip install requests
pip install chardet
pip install brotli

conda install requests
'''

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code'
param = {'code': 161967}
response = requests.get(url, params=param)
print(response.text)