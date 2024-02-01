# date : 20240201
# file : test25_web.py
# desc : urlib 모듈 사용법

# from urllib.request import *  >> 의미 : request 모듈 안에 있는 모든 내용을 다 사용 할 때.
from urllib.request import Request, urlopen  # Request 클래스와 urlopen만 사용 하겠다는 의미

red = Request('https://www.naver.com/') # 네이버 웹 주소 URL
res = urlopen(red) # URL 주소로 웹사이트를 열어달라고 요청

print(f'응답코드 : {res.status}') # URL로 요청된 웹사이트 응답 확인
print(res.read())

# urllib.requet보다 성능이 조금 더 나은 모듈
import requests

red2 = requests.get('https://www.naver.com/')
print(f'응답코드? : {red2.status_code}')
print(red2.text)