# date : 20240130
# file : test14.while.py
# desc : while

## while 참인 조건 :
## 공통점 if 조건 : else 조건 : , for in rnage() : while 조건

count = 0

# while count < 0 : # count 변수값이 10보다 작거나 같을 동안 반복

# 무한루프 : Window os, 모바일 os, 네비게이션, 라즈베리파이, 아두이노, 게임 ... 사용
while True : # 참인동안 True 항상 참 무한루프
    count = count + 1
    print('나무찍기', count)
    if count == 10 :
        break # 조건을 만족 했을 때 반복문 종료

number = 0
while True :
    number = number + 1
    if str(number) in ['3', '6', '9'] :
        print('짝!')
    else :
        print(number)
        
    if number == 30 : break