num_reversed = input()
num = ''
for x in range(len(num_reversed)-1, -1, -1): num+=num_reversed[x]

for x in range(1,int(num[0])+1):
    for y in range(1,int(num[1])+1):
        for z in range(1,int(num[2])+1):
            print(f'{x} * {y} * {z} = {x*y*z};')