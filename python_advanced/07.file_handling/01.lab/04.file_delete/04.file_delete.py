import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','03.file_writer','03.my_first_file.txt')

os.remove(FILE_PATH)