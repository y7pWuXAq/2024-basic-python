# date : 20240130
# desc : if문 응용

import datetime

now = datetime.datetime.now() # 현재 년, 월, 일, 시, 분, 초 가져옴

if now.hour < 12 : 
    print('오전입니다.')
else : # now.hour >= 12 : << if 함수 사용 시 기재, else 사용 시 생략
    print('오후입니다.')