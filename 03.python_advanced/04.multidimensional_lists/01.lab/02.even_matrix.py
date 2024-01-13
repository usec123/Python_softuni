rows = int(input())
matrix = [[num for num in list(map(int,input().split(', '))) if num%2==0] for _ in range(rows)]
print(matrix)