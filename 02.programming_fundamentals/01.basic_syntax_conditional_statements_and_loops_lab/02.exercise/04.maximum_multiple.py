divisor = int(input())
boundary = int(input())
largest = 0
for x in range(boundary+1):
    if x % divisor == 0: largest = x
print(largest)