import re
import os
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'text.txt')

with open(FILE_PATH) as file:
    lines = file.readlines()

    for x in range(len(lines)):
        if x%2==0:
            print(' '.join(re.sub(r'[-,.!?]','@',lines[x]).split()[::-1]))