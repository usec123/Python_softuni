n = int(input())

cnt = 1
num = 1

while num<=n:
    res = ''
    for y in range(cnt):
        res += str(num) + ' '
        num += 1
        if num > n: break
    print(res)
    cnt+=1