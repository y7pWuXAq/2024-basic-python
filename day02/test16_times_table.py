# date : 20240130
# file : test16_times_table.py
# desc : 구구단 프로그램
# spec : for문 활용, 2중 for문의 이해
# debugging : f9(중단점 토글), f5(디버그시작), f10(한줄씩 실행), f11(함수안으로 진입) > 이후 조사식 확인

# 2 x 1 = 2, 2 x 2 = 4 ... 2 x 9 = 18
# 9 x 1 = 9, 9 x 2 = 18 ... 9 x 9 = 81

x = 2 
for y in range(1, 9+1) : 
    print(f'{x} x {y} = {x*y:2d}') ## 2단만

print('구구단 시작~!')
for x in range(2, 3+1) :
    print(f'{x}단 > ')
    for y in range(1, 9+1) : 
        print(f'{x} x {y} = {x*y:2d}', end =' ') ## 2중 for문을 활용한 2~9단까지. // end = ' ' > 엔터를 공백으로 변경
    print() # 안쪽 for문이 끝나면 마지막에 줄바꿈