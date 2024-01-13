rows = int(input())
matrix = [[num for num in list(map(int,input().split(', ')))] for _ in range(rows)]
print([num for sublist in matrix for num in sublist])