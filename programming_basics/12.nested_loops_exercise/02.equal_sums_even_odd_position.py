num1 = int(input())
num2 = int(input())

result = ''

for x in range(num1, num2+1):
    sumodd = 0
    sumeven = 0
    y = str(x)
    for z in range(0,len(y)):
        zz = int(y[z])
        if z%2==0: sumodd += zz
        else: sumeven+=zz
    if sumodd == sumeven: result+=str(x) + ' '
print(result)