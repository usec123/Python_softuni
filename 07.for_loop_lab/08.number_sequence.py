from math import inf

max = -inf
min = inf

n = int(input())
for x in range(0,n):
    num = int(input())
    if (num > max): max = num
    if (num < min): min = num

print(f'Max number: {max}\nMin number: {min}')