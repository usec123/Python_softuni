#print(' '.join(list(map(int,input().split()))[::-1]))

stack = [int(item) for item in input().split()]

while stack:
    print(stack.pop(),'',end='')