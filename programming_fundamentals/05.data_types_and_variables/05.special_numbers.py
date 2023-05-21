n = int(input())
for num in range(1,n + 1):
    sum = 0
    for char in str(num): sum+=int(char)
    print(f'{num} -> {sum in [5, 7, 11]}')