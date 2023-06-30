number = int(input())
position = int(input())

mask = 7<<position
temp = number^mask
print(temp)