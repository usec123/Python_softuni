n = int(input())
sumodd = 0
sumeven = 0

for x in range(1,n+1):
    if x%2==0: sumeven += int(input())
    else: sumodd += int(input())

if sumeven == sumodd: print(f'Yes\nSum = {sumodd}')
else: print(f'No\nDiff = {abs(sumodd - sumeven)}')