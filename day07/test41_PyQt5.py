# date : 20240207
# file : test41_PyQt5.py
# desc : PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget) :

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) :
        # 이미지 추가 scaledToWidth() : 큰 해상도 넓이를 ()안의 숫자로 고정
        pixmap = QPixmap('./images/kitty.png').scaledToWidth(800)
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(self)
        lblSize.setFont(QFont('NanumGothicCoding', 13)) # 폰트와 폰트 사이즈
        lblSize.setStyleSheet('Color : #ff99cc;') # 폰트 색상
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}') # 추가한 사진의 넓이 높이
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로 중앙 정렬 | 세로 중앙 정렬

        vbox = QVBoxLayout(self) # QtDesigner VerticalLaout 위젯 생성
        vbox.addWidget(lblImage) # VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # From에 VL 추가와 동일

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300, 300, 300, 300) # x, y, w, h
        self.setGeometry(rect) ## 같은 이름의 함수를 여러개 선언 후 상황에 맞게 골라서 사용하는 BR
        self.show() # showFullScreen() : 모니터를 꽉 채워서 출력
        self.setCenter()
    
    def setCenter(self) : # 만들어진 윈앱을 화면 정 중앙에 위치시키는 함수
        gm = self.frameGeometry() # 현재 윈앱 자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height() # 활용도 높음
    print(width, 'X', height)
    ins = WinApp()
    sys.exit(app.exec_()) # 종료 시 리소스 반환 등 효율을 위해 사용