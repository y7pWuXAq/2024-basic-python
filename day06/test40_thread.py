# date : 20240206
# file : test40_thread.py
# desc : Qt 스레드로 동작

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread) : # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI 스레드로 전달하기 위한 변수 객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None :
        super().__init__(parent) 
        self.parent = parent # BackWorker에서 사용할 멤버변수
    
    def run(self) -> None : # 스레드 실행
        # 스레드로 동작 할 내용
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        # self.parent.pgbTask.setValue(0) # 프로그래스바 0부터 시작 // QThread 에선 관련 UI 처리XX
        # self.parent.pgbTask.setRange(0, maxVal-1) # 0부터 100까지
        for i in range(maxVal) :
            print_str = f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            # self.parent.txbLog.append(print_str)
            # self.parent.pgbTask.setValue(i)

class qtwin_exam(QWidget) :
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner에서 만든 UI를 불러오기
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # UI 파일 안에 있는 위젯 접근은 VSCode 상에서 색상으로 표시X

    def btnStartClicked(self) :
        th = BackWorker(self)
        th.start() # BackWorker 안에 있는 self.run()이 실행이 된다.
        th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 함수가 대신 처리
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxbLog) # TextBrower 위젯에 진행사항 출력


    def closeEvent(self, QCloseEvent) -> None: # 프로그램 종료 확인
        re = QMessageBox.question(self, '종료확인', '종료?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫기
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()

    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯 함수
    @pyqtSlot(int) # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
    def initPgbTask(self, maxVal) :
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)

    @pyqtSlot(str) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
    def setTxbLog(self, msg) :
        self.txbLog.append(msg)
    
    @pyqtSlot(int)
    def setPgbTask(self, val) :
        self.pgbTask.setValue(val)


if __name__ == '__main__' :
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()