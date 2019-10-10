import os
import sys
import importlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

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
        wg = MainPageWidget()
        self.setCentralWidget(wg)
        self.statusBar().showMessage('Ready')
        self.setGeometry(200,200,1000,700)
        self.show()

class MainPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Indian Poker')
        self.resize(1000, 700)
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(10, 10)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.show()


if __name__ == '__main__':
    path2 = 'aicode.demo_ai'
    a = load_module(path2)
    print(a.test())
    GameStart()