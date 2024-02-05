# date : 20240206
# file : test38_PyQy5.py
# desc : QtDesigner로 만든 UI와 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget) :
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui', self) # QtDesigner에서 만든 UI를 불러오기
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # UI 파일 안에 있는 위젯 접근은 VSCode 상에서 색상으로 표시X
        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self) :
        print('시작 버튼 클릭')
        self.lblSratus.setText('상태 : 동작 시작')
        QMessageBox.about(self, '동작', '시작되었습니다.')

    def btnStopClicked(self) :
        print('종료 버튼 클릭')
        self.lblSratus.setText('상태 : 동작 중지')

    def closeEvent(self, QCloseEvent) -> None: # 프로그램 종료 확인
        re = QMessageBox.question(self, '종료확인', '종료?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫기
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()
    

if __name__ == '__main__' :
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()