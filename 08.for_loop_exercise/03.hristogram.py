n = int(input())

d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0

for _ in range(0,n):
    a = int(input())
    if a<200: d1 += 1
    elif a<400: d2+=1
    elif a<600: d3+=1
    elif a<800: d4+=1
    else: d5+=1

print(f'{d1/n*100:.2f}%')
print(f'{d2/n*100:.2f}%')
print(f'{d3/n*100:.2f}%')
print(f'{d4/n*100:.2f}%')
print(f'{d5/n*100:.2f}%')