n = int(input())

res = ''

for x in range(1111,10000):
    special = True
    x = str(x)
    for y in x:
        if y!='0': 
            if n%int(y)!=0: special = False
        else: special = False
    if special: res += str(x) + ' '
print(res)