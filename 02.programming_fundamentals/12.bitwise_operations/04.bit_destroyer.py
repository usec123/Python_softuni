number = int(input())
position = int(input())
mask = ~ (1 << position)
number = number & mask
print(number)