# date : 20240207
# file : test42_pyppaint.py
# desc : 그림판 만들기

import sys
from PyQt5 import uic # QtDesigner 호출 시 필요
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget) :
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self) : # 화면 초기화
        # uic.loadUi('./day07/pyPaint.ui', self)
        uic.loadUi('pyPaint.ui', self) # 실행파일 생성시는 경로에 상대경로가 없어져야함
        # self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowIcon(QIcon('iot.png'))
        self.setWindowTitle('Py 그림판')
       
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')

        self.show()
        self.setCenter()
    
    def initSignal(self) :
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        # 20240206 버튼 추가
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)

    def btnLoadClicked(self) :
        image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg *.png)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(380) # 파일 경로에 있는 이미지를 읽어서 pixmap 객체에 담기
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 라벨크기에 맞추기

    def btnSaveClicked(self) :
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.jpg *.png)')
        if filePath == '' : return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)


    def buttonClicked(self) : # 세가지 색을 다 통일한 함수
        btn_val = self.sender().objectName()
        print(btn_val)
        
        # def 주석 부분 요약 함수
        if btn_val == 'btn_black' : # 검은 버튼 클릭
            self.brushColor = Qt.black
        elif btn_val == 'btn_red' : # 빨간 버튼 클릭
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue' : # 파란 버튼 클릭
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear' : # 버튼 클리어
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)


    # def btnBlackClicked(self) :
    #     btn_val = self.sender().objectName() # self.sender()에 입력된 값은 btn_blue
    #     print(btn_val)
    #     self.brushColor = Qt.black

    # def btnRedClicked(self) :
    #     btn_val = self.sender().objectName()
    #     print(btn_val)
    #     self.brushColor = Qt.red

    # def btnBlueClicked(self) :
    #     btn_val = self.sender().objectName()
    #     print(btn_val)
    #     self.brushColor = Qt.blue

    # def btnClearClicked(self) :
    #     btn_val = self.sender().objectName()
    #     print(btn_val)
    #     self.canvas.fill(QColor('white'))
    #     self.lb_canvas.setPixmap(self.canvas)


    def mouseMoveEvent(self, e) -> None :
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap())
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update() # 화면 업데이트


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