numbers = list(map(int,input().split()))
target = int(input())

x = 0

while x in range(len(numbers)):
    for y in range(x+1,len(numbers)):
        if numbers[x]+numbers[y] == target:
            print(f'{numbers[x]} + {numbers[y]} = {target}')
            numbers.pop(x)
            numbers.pop(y-1)
            x-=1
            break
    x+=1