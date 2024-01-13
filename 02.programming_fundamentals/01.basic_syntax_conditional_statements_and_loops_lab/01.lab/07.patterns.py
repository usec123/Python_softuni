num = int(input())

for x in range(0,num):
    for y in range(-1,x):
        print('*', end='')
    print()
for x in range(num-1,0,-1):
    for y in range(0,x):
        print('*', end='')
    print()