rows, columns = list(map(int,input().split(', ')))
matrix = [list(map(int,input().split(', ')))[:columns:] for _ in range(rows)]
print(sum(sum(m) for m in matrix))
print(matrix)