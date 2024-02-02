# date : 20240131
# file : test23_module.py
# desc : 모듈 사용

import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')

print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2 ** 10)
print(math.pow(2,10))
print(math.ceil(3.1)) # 올림
print(math.floor(3.5)) # 내림
print(round(3.5)) # 반올림 (자주 사용해서 기본 함수에 있음)

import math as m # 별명짓기 : as
print(m.sin(2))

from math import pi, pow # 주의해서 사용해야 함 // from ~~ pi랑 pow 만 쓰겠다는 의미
print(pi)
print(pow(2,10))