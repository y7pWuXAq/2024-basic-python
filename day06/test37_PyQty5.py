# date : 20240206
# file : test37_PyQy5.py
# desc : PyQy5 이벤트(Signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget) :
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) :
        btn01 = QPushButton('클릭', self)
        btn01.setGeometry(50, 100, 100, 40)
        btn01.clicked.connect(self.btn01_clicked) # 버튼을 클릭하면(Signal) btn01_clicked 함수를 실행하겠다.

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('버튼 시그널')
        # self.show()
    
    def btn01_clicked(self) :
        QMessageBox.about(self, '버튼클릭', '버튼을 클릭했습니다!')

    # QWidget에 있는 CloseEvent를 그대로 쓰면 닫기 버튼 클릭 시 그냥 종료 됨
    # 닫기 확인 팡을 물어보는 형태로 재정의 : Overrride
    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫기
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()

if __name__ == '__main__' : # Main entry 확인 조건 추가
    loop = QApplication(sys.argv) # 내 소스의 위치로 앱을 생성한다는 의미
    instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
    instance.show() # 22줄에 있는 self.show() 와 동일한 의미
    loop.exec_()