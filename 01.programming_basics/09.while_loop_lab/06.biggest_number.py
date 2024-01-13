from math import inf

num = input()
max = -inf

while num!='Stop':
    if int(num)>max: max = int(num)
    num = input()

print(max)