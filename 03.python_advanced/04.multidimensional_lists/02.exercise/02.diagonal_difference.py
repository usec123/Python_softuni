size = int(input())

matrix = [[int(item) for item in input().split()[:size:]] for _ in range(size)]

primary_diagonal = [matrix[x][x] for x in range(size)]
secondary_diagonal = [matrix[x][-(x+1)] for x in range(size)]

print(abs(sum(primary_diagonal)-sum(secondary_diagonal)))