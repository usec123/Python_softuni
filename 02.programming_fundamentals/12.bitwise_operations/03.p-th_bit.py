num = int(input())
position = int(input())
mask = 1 << position
result = num & mask
lsb = result >> position
print(lsb)