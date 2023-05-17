n = int(input())
sum1 = 0
sum2 = 0
for x in range(0,2*n):
    if x<n: sum1+=int(input())
    else: sum2+=int(input())

if sum1 == sum2: print(f'Yes, sum = {sum1}')
else: print(f'No, diff = {abs(sum1-sum2)}')