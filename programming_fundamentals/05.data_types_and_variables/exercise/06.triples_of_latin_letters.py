a_num = ord('a')
n = a_num - 1 + int(input())
output = [a_num,a_num,a_num]
while output[0] <= n and output[1] <= n and output[2] <= n:
    for x in output: print(chr(x),end='')
    print()
    output[2]+=1
    for x in range(1,-1,-1):
        if output[x+1] > n:
            output[x+1] = a_num
            output[x] += 1