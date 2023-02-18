from math import inf

a = int(input())

max = -inf
sum = 0

for x in range(0,a):
    y = int(input())
    if y > max: max = y
    sum+=y
sum-=max

if sum == max: print(f'Yes\nSum = {sum}')
else: print(f'No\nDiff = {abs(sum-max)}')