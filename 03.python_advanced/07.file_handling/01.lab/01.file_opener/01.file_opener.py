import os

try:
    FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'01.text.txt')
    file = open(FILE_PATH)
    print('File found')
except FileNotFoundError:
    print('File not found')
finally:
    file.close()