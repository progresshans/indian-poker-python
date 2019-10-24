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
        
        self.ai_1 = self.ai_push_button_1.clicked.connect(self.ai_load_1)
    
    def ai_load_1(self):
        ai_name = self.ai_input_1.text()
        print(ai_name)
        self.ai_log_1.clear()
        self.ai_log_1.append(f'{ai_name}.py를 로드합니다.')
        
        try:
            ai_path = f'aicode.{ai_name}'
            ai = load_module(ai_path)
            self.ai_log_1.append(f'{ai_name}가 정상적으로 로드되었습니다.')
            return ai
        except:
            self.ai_log_1.append('해당 이름의 Ai 코드가 없습니다.')
            return False

    def ai_load_2(self):
        pass

if __name__ == '__main__':
    path2 = 'aicode.demo_ai'
    a = load_module(path2)
    print(a.test())
    GameStart()