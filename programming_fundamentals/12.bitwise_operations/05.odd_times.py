numbers = list(map(int,input().split()))

checking = numbers[0]
x = 1

while len(numbers)>1 and x < len(numbers):
    if numbers[x] ^ checking == 0:
        checking = numbers[1]
        numbers.pop(x)
        numbers.pop(0)
        x = 0
    x+=1
    
print(numbers[0])