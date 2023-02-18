from math import inf

num = input()
min = inf

while num!='Stop':
    if int(num)<min: min = int(num)
    num = input()

print(min)