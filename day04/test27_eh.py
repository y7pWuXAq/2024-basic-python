# date : 20240201
# file : test27_eh.py
# desc : 예외발생 처리

def add(x, y) :
    return x + y

def minus(x, y) :
    return x - y

def multi(x, y) :
    return x * y

def divide(x, y) : 
    try :
        return x / y # 분모를 0으로 입력 시 예외발생(ZeroDivisionError)
    except ZeroDivisionError as e :
        print('[!!오류!!] 0으로 나눌 수 없습니다.')
        return 0

def getOperands() : # 계산 할 수를 입력받는 함수 / 중복되는 항목은 함수로 만들면 편하다
    # 소숫점을 입력 했을 때 예외발생(ValueError)
    try :
        a, b = map(int,input('두 수를 입력하세요(구분자 공백) > ').split())
        return a,b
    except ValueError as e :
        # print(e) # 정확한 예외 메시지 출력
        print('입력 오류 : 정수만 입력하세요.')
        return 1, 1

while True :
    mnu = input('메뉴 입력(p[더하기],m[빼기],t[곱하기],d[나누기], x[종료]) > ')

    if mnu == 'p' :
        a, b = getOperands()
        print(f'더하기 결과 {a} + {b} = {add(a,b)}')
    elif mnu == 'm' :
        a, b = getOperands()
        print(f'빼기 결과 {a} - {b} = {minus(a,b)}')
    elif mnu == 't' :
        a, b = getOperands()
        print(f'곱하기 결과 {a} x {b} = {multi(a,b)}')
    elif mnu == 'd' :
        a, b = getOperands()
        print(f'나누기 결과 {a} ÷  {b} = {divide(a,b)}')
    elif mnu == 'x' :
        break
    else :
        continue # 다시 메뉴 선택으로 올라감
