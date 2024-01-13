import os

email = 'some_email@abv.bg'

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'00.users.txt')

file = open(FILE_PATH, 'w')
# first arg is the path
# second arg is the mode: 'r'eadonly (default), 'w'rite, 'a'ppend, 't'ext, 'b'inary, '+' - read and write

file.write(email)

file.close()

file = open(FILE_PATH, 'a') # append

file.write(' # appended text')

file.write('\n# more appended text')

file.close()

# file.read(2) -> reads only 2 symbols from file

file = open(FILE_PATH, 'r')

# read continues from last read operation
print(file.read(2)) # so
print(file.read(2)) # me

file.close()

file = open(FILE_PATH, 'r')

for line in file:
    print(line, end='')
    
file.close()


# with statement -> closes file after execution
with open(FILE_PATH, 'a') as f:
    f.write('\nHello')