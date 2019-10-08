import os
import sys
import importlib

path = "./aicode/"
file_list = os.listdir(path)
ai_file_py = [file for file in file_list if file.endswith(".py")]

def load_module(module_name):
    mod = importlib.import_module(module_name)
    return mod

class GameStart:
    pass


a = load_module(f'aicode.demo_ai')
print(a.test())