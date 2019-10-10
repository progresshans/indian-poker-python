import os
import sys
import importlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

main_window = uic.loadUiType("mainwindow.ui")[0]

def load_module(module_name):
    mod = importlib.import_module(module_name)
    return mod

class GameStart:
    def __init__(self):
        app = QApplication(sys.argv)
        ex = MainWindow()
        sys.exit(app.exec_())

class MainWindow(QMainWindow, main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
    path2 = 'aicode.demo_ai'
    a = load_module(path2)
    print(a.test())
    GameStart()