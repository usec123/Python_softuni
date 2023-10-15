import os
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'03.my_first_file.txt')

with open(PATH,'w') as file:
    file.write('I just created my first file!')