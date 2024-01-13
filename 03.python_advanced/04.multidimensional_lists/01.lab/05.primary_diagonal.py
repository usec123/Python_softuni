size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(map(int,input().split()[:size:])))

print(sum([matrix[x][x] for x in range(size)]))