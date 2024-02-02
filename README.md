# 파이썬 기초 2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어 - 파이썬


## 1일차
- 개발환경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - tortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자
    ```python
    # 주석
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01)
    print(type(var01)) # <class of 'int'>

    print(5 + 4 / 2) # 7.0
    print(5 == 4) # False
    ```


## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참과 거짓으로 구분하기 (다른언어 switch)
        - for : 반복문의 기본 구조 (다른언어 foreach)
        - while : 반복문 변형 (다른언어 do ~ while)
    - 복합자료형 + 연산자(연산함수)
    - 출력 포맷
    - 구구단 + 디버깅
```python
# debugging : f9(중단점 토글), f5(디버그시작), f10(한줄씩 실행), f11(함수안으로 진입) > 이후 조사식 확인

print('구구단 시작~!')
for x in range(2, 9+1) : # 2단부터 9단까지 반복
    print(f'{x}단 > ')
    for y in range(1, 9+1) : # 1부터 9까지 반복
        print(f'{x} x {y} = {x*y:2d}', end =' ') ## 2중 for문을 활용한 2~9단까지. // end = ' ' > 엔터를 공백으로 변경
    print() # 안쪽 for문이 끝나면 마지막에 줄바꿈
```


## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기
    - 함수, 람다 함수는 나중에 ... 
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화(__plateNumber)
    - 패키지, 모듈


## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        - pip 사용
        ```shell
        > pip -- version # 버전확인
        > pip list # 현재 설치 된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지 삭제
        ```

    - 예외처리 : 비정상적인 프로그램 종료 막기
    ```python
    def divide(x, y) : 
        try :
            return x / y # 분모를 0으로 입력 시 예외발생(ZeroDivisionError)
        except ZeroDivisionError as e :
            print('[!!오류!!] 0으로 나눌 수 없습니다.')
            return 0
    ```

    - 텍스트 파일 입출력
    ```python
    f = open('파일명', mode='r(읽기)'/'w(쓰기)'/'a(내용추가)', encoding='cp949(한국어)'/'utf-8(만국 공통어)')
    f.read()
    f.readline() # 읽기
    f.write('text', 'text\n(끝에 줄바꿈)') # 쓰기
    f.close() # 파일은 반드시 닫는다.
    ```

- 파이썬 응용
    - 주피터 노트북
        - ctrl + shift + P(명령 팔레트)로 시작
        - 사용방법 (test31_jupyternb.ipynb) 참조.
    - folium 기본 사용
    ![folium사용법](https://raw.githubusercontent.com/y7pWuXAq/basic-python-2024/main/images/python_001.png)


## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 구글 코랩(Colab)