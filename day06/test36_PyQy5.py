# date : 20240206
# file : test36_PyQy5.py
# desc : PyQy5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
## GUI : Graphic User Interface <-> CLI : Command Line Interface
from PyQt5.QtWidgets import QApplication, QWidget
# print(sys.argv) # 현재 파이썬 파일의 경로 표시

class qtwin_exam(QWidget) : # Qwidget을 상속 받는다는 의미 > QWidget이 가진 모든것을 사용할 수 있다.
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI() # 화면 초기화 함수를 호출
    
    def initUI(self) :
        self.setGeometry(1920//2, 1080//2, 400, 300) # x, y, width, heignt
        self.setWindowTitle('Qy5 Hello World!')
        self.text = '' # 글자를 적을 수 있는 위치
        self.show()
    
    def drawText(self, event, paint) :
        paint.setPen(QColor(10, 10, 10)) ## 기본 RGB 색상, 0부터 255까지
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText(290//2, 300//2, 'HELL World!')
        paint.drawText(event.rect(), Qt.AlignLeft, self.text) #AligenLeft > 글자 정렬 방식

    def paintEvent(self, event) -> None : # 재정의(Override)
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() # 닫는다


loop = QApplication(sys.argv) # 내 소스의 위치로 앱을 생성한다는 의미
instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
loop.exec_()