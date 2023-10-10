rows, columns = list(map(int,input().split(', ')))
matrix = [list(map(int,input().split(' ')))[:columns:] for _ in range(rows)]

for x in range(columns):
    print(sum([matrix[row][x] for row in range(rows)]))