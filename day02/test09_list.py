# date : 20240130
# desc : 복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60

# koreansum = s1 + s2 + s3 + s4 + s5
# print(koreansum)
# print(koreansum / 5) ## 학생 수만큼 변수를 생성 한 예제 비효율적임

## inedx = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ... n // 모든 index의 값은 0부터 시작
## 총 갯수가 n개일 경우 index의 마지막 값은 n-1개
## index = -n ... -4, -3, -2, -1 // -값으로 표현해도 가능(python만)

std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100] # 리스트로 변수 생성

print(std[9])

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3,4), std] ## python 리스트의 장점!
print(list_1)
print(list_1[5])
list_1[6] = '바꾼 값' ## 값을 바꿀 때도 [] 활용하여 값을 할당 할 수 있음.
print(list_1)

## 리스트 연산
print(list_1[2 : 4]) # 출력하고 싶은 범위 리스트 값은 [index : index+1] 하기.
print(list_1[-5 : -3]) # -index도 가능, 다만 되도록 사용 X

## 이중 리스트
# 리스트 안에 리스트가 있을 경우 index 값 가져오기
list_2 = [[1,2,3], [4,5,6], [7,8,9]] 
print(list_2[1][2]) #[변수 리스트의 index 값][선택한 리스트의 index 값]

## 리스트 연산 +, * 만 사용 가능
list_3 = [1,2,3]
list_4 = [7,8,9]

print(list_3 + list_4) # '+' 리스트를 연결할 때 사용
print(list_3 * 2) # '*' 리스트를 반복할 때 사용

## 리스트 길이함수 len()
print(len(list_3))

## append() : 리스트 마지막에 입력값을 추가하는 함수
## insert(index, val) : 리스트의 index에 val을 삽입하는 함수
print(list_1)

list_1.append('Hello!!')
print(list_1)

list_1.insert(2, 100) # 기존 값은 추가 값 뒤로 밀림.
print(list_1)

## extend() : 기존 리스트 확장
list_3.extend(list_4) # 리스트 연산 '+'는 일회성, extend()는 합한 값을 저장
print(list_3)
print(list_4)

## 리스트 삭제 : del
del list_3[3] # 리스트의 index를 삭제
print(list_3)
# del list_3 # 리스트 자체를 삭제

val = list_4.pop() # 리스트의 마지막 값을 꺼내오기.
print(val)
print(list_4)

print(std)
val = std.pop(2)
print(val)
print(std)

## clear() : 리스트 클리어
list_4.clear() # del() 은 리스트 완전 삭제 , clear() 리스트 내용만 삭제
print(list_4)

## sort() : 리스트 정렬
print(list_1)
# list_1.sort() # 문자열, 숫자열, 불 섞여있는 리스트는 정렬 할 수 없다.

std.sort() # 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

## in, not in : 리스트 안에 값을 찾을 때
print(99 in std) # True
print(98 in std) # False

## reverse(), copy(), count() ... 그 외 함수들

## * 리스트 : 전개연산자
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)