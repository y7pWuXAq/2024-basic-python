# date : 20240131
# file : test21_oop.py
# desc : 객체지향 클래스 만들기

# 클래스 만들기 (사람이라는 객체를 만들기 위한 청사진)
class Person : # 사람 클래스 선언
    name = '' # 멤버변수
    age = 0
    gender = ''

    # 생성자 함수(스페셜 함수) : 클래스의 객체를 생성할 때 동작.
    # init == initialization(초기화)
    def __init__(self) -> None :
        self.name = '홍길동'
        self.age = 29
        self.gender = 'male'

    # 클래스를 호출할 때 원하는 형태로 변환해서 보여줄 때 사용
    def __str__(self) -> str :
        strs = f'커스텀 출력, 이름{self.name} 객체 생성.'
        return strs
   
    def walk(self) : # 멤버 함수 매개변수 self 필수!
        print(f'{self.name}이(가) 걷습니다.')
    
    def stop(self) :
        print(f'{self.name}이(가) 멈춥니다.')

# 사람 객체 생성, Instance(사례, 예제)
sw = Person()
yr = Person()

# print(type(sw))
# print(id(sw)) # 다른 객체인지 확인 할 때 사용
# print(id(yr))

sw.name = "함소화" # 객체명.멤버변수 = ... << 양식
sw.age = 27
sw.gender = 'Female'

yr.name = '서여름'
yr.age = 27
yr.gender = 'male'

print(f'sw => 이름:{sw.name} / 나이:{sw.age} / 성별:{sw.gender}')
print(f'yr => 이름:{yr.name} / 나이:{yr.age} / 성별:{yr.gender}')

sw.walk()
print('1분동안 걷는다.')
sw.stop

yr.walk()
print('걷기 싫어함.')
yr.stop()

print('생성자 함수 추가 --- > ')
gd = Person()
print(f'gd => 이름:{gd.name} / 나이:{gd.age} / 성별:{gd.gender}')
print(gd)