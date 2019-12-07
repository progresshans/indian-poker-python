import os
import sys
import importlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

main_window , _ = uic.loadUiType("mainwindow.ui")
game_window, _ = uic.loadUiType("gamewindow.ui")

def load_module(module_name):
    mod = importlib.import_module(module_name)
    return mod

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.startMainWindow()

    def startMainWindow(self):
        self.ui = main_window()
        self.ui.setupUi(self)
    
        self.ai_1 = False
        self.ai_2 = False
        
        self.ui.ai_push_button_1.clicked.connect(self.ai_load_1)
        self.ui.is_not_ai_1.stateChanged.connect(self.ai_1_is_ai)
        self.ui.ai_push_button_2.clicked.connect(self.ai_load_2)
        self.ui.is_not_ai_2.stateChanged.connect(self.ai_2_is_ai)
        self.ui.setting_done_button.clicked.connect(self.setting_done)

    def startGameWindow(self):
        self.ui = game_window()
        self.ui.setupUi(self)

    def ai_load_1(self):
        ai_name = self.ui.ai_input_1.text()
        self.ui.ai_log_1.clear()
        self.ui.ai_log_1.append(f'{ai_name}.py를 로드합니다.')
        
        try:
            ai_path = f'aicode.{ai_name}'
            ai = load_module(ai_path)
            self.ui.ai_log_1.append(f'{ai_name}가 정상적으로 로드되었습니다.')
            self.ai_1 = ai
        except:
            self.ui.ai_log_1.append('해당 이름의 Ai 코드가 없습니다.')
            self.ai_1 = False

    def ai_1_is_ai(self, state):
        if state:
            self.ui.ai_log_1.clear()
            self.ui.ai_log_1.append('사람이 플레이합니다.')
            self.ai_1 = 'Person'
            self.ui.ai_input_1.setReadOnly(True)
            self.ui.ai_push_button_1.setEnabled(False)
        else:
            self.ui.ai_log_1.clear()
            self.ui.ai_log_1.append('첫번째 Ai가 로드되지 않았습니다.')
            self.ai_1 = False
            self.ui.ai_input_1.setReadOnly(False)
            self.ui.ai_push_button_1.setEnabled(True)

    def ai_load_2(self):
        ai_name = self.ui.ai_input_2.text()
        self.ui.ai_log_2.clear()
        self.ui.ai_log_2.append(f'{ai_name}.py를 로드합니다.')
        
        try:
            ai_path = f'aicode.{ai_name}'
            ai = load_module(ai_path)
            self.ui.ai_log_2.append(f'{ai_name}가 정상적으로 로드되었습니다.')
            self.ai_2 = ai
        except:
            self.ui.ai_log_2.append('해당 이름의 Ai 코드가 없습니다.')
            self.ai_2 = False

    def ai_2_is_ai(self, state):
        if state:
            self.ui.ai_log_2.clear()
            self.ui.ai_log_2.append('사람이 플레이합니다.')
            self.ai_2 = 'Person'
            self.ui.ai_input_2.setReadOnly(True)
            self.ui.ai_push_button_2.setEnabled(False)
        else:
            self.ui.ai_log_2.clear()
            self.ui.ai_log_2.append('첫번째 Ai가 로드되지 않았습니다.')
            self.ai_2 = False
            self.ui.ai_input_2.setReadOnly(False)
            self.ui.ai_push_button_2.setEnabled(True)

    def setting_done(self):
        self.ui.ai_log_1.append(f'{self.ai_1}')
        self.ui.ai_log_2.append(f'{self.ai_2}')

        if self.ai_1 == False:
            QMessageBox.about(self, "에러", "첫번째 Ai에 대한 설정이 없습니다. 사람이 플레이하려면 체크박스에 체크를 하세요.")
        elif self.ai_2 == False:
            QMessageBox.about(self, "에러", "두번째 Ai에 대한 설정이 없습니다. 사람이 플레이하려면 체크박스에 체크를 하세요.")
        else:
            self.startGameWindow()
        
if __name__ == '__main__':
    path2 = 'aicode.demo_ai'
    a = load_module(path2)
    print(a.test())
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())