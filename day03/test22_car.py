# date : 20240131
# file : test22_car.py
# desc : Car 클래스 만들기

class Car :
    wheel_num = 4
    color = 'white'
    plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전
    def moveForward(self) :
        print(f'{self.plate_num}이 전진합니다.')

    def moveBackward(self) :
        print(f'{self.plate_num}이 후진합니다.')

    def moveLeft(self) :
        print(f'{self.plate_num}이 좌회전합니다.')

    def moveRight(self) :
        print(f'{self.plate_num}이 우회전합니다.')

    # 생성자를 변경했으니까 변경된 생성자로 호출 해야함.
    def __init__(self, plate_num, company, color, gear_type) -> None:
        self.plate_num = plate_num
        self.company = company
        self.color = color
        self.gear_type = gear_type

    def __str__(self) -> str: # print(객체) 출력되는 부분 지정
        return f'제 차는 {self.plate_num} 입니다. {self.color} 입니다.'


sarah = Car('54라9538', '현대자동차', '흰색', '자동')
print(sarah)
print(f'차 번호는 {sarah.plate_num}')
print(f'차 색상은 {sarah.color}')
sarah.moveForward()

csuv = Car('경남88가1922', '기아자동차', '회색', '자동')
print(f'차 번호는 {csuv.plate_num}')