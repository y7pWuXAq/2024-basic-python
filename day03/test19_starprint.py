# date : 20240131
# file : test19_starprint.py
# desc : 별찍기 또는 피라미드 만들기

for i in range(1, 5+1) : # 2중 for문
    for j in range(1, i+1) :
        # i가 1일 때 : range(1,2) > 1회 반복
        # i가 2일 때 : range(1,3) > 2회 반복
        # ...
        print('*', end='') # end='' : 줄바꿈 대신 empty로 변환
    print() # 의미 : 안쪽 for문이 끝나면 줄바꿈

for i in range(1, 5+1) :
    for j in range(1, 6-i+1) :
        print('*', end='')
    print()