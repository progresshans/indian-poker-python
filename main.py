import os
import sys
import importlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def load_module(module_name):
    mod = importlib.import_module(module_name)
    return mod

class GameStart:
    def __init__(self):
        app = QApplication(sys.argv)
        ex = MainWindow()
        sys.exit(app.exec_())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        pswg = PreviousSettingPage()
        self.setCentralWidget(pswg)

        self.statusBar().showMessage('원본 코드 :  https://github.com/progresshans/indian-poker-python')
        self.setGeometry(200,200,1000,700)
        self.show()
    
    def change_page(self):
        if value == 0:
            wg = PreviousSettingPage()
            setCentralWidget(wg)
        elif value == 1:
            wg = MainPage()
            self.setCentralWidget(self.wg)

class PreviousSettingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Indian Poker Setting')
        self.resize(1000, 700)
        self.initUI()
        self.show()

    def initUI(self):
        btn = QPushButton('확인', self)
        btn.move(10, 10)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.enter_clicked)

    def enter_clicked(self):
        MainWindow.change_page(1)


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Indian Poker')
        self.resize(1000, 700)
        self.initUI()
        self.show()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(10, 10)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)



if __name__ == '__main__':
    path2 = 'aicode.demo_ai'
    a = load_module(path2)
    print(a.test())
    GameStart()