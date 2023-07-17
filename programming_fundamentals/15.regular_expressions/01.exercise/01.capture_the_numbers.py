import re

found = []
cmd = input()
pattern = r'\d+'
while cmd:
    for x in re.findall(pattern,cmd):
        found.append(x)
    cmd = input()
print(' '.join(found))