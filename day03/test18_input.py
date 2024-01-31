# date : 20240131
# file : test18_input.py
# desc : 다중 입력
# 원래는 (in_a, in_b) 튜플형 데이터를 받는게 정석이나 생략함

# 1. 두 수를 받을 때 가장 기본적인 방법
# input_a, input_b = input('두개의 값을 입력 (공백으로 구분) > ').split(' ')
# input_a = int(input_a)
# input_b = int(input_b)
# print(f'입력값 {input_a}, {input_b}')
# print(f'더하기 결과 {input_a + input_b}')

# 2. map() 함수 사용
input_a, input_b = map(int, input('두개의 값을 입력 (공백으로 구분) > ').split(' '))
print(f'입력값 {input_a}, {input_b}')
print(f'더하기 결과 {input_a + input_b}')