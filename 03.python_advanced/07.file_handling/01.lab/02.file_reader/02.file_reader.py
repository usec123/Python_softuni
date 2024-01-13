import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'02.numbers.txt')

file = open(FILE_PATH)

sum = 0

for line in file:
    sum+=int(line)

file.close()

print(sum)