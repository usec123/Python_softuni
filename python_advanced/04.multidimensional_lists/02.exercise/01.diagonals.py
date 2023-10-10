size = int(input())

matrix = [[int(item) for item in input().split(', ')[:size:]] for _ in range(size)]

main_diagonal = [matrix[x][x] for x in range(size)]
secondary_diagonal = [matrix[x][-(x+1)] for x in range(size)]

print(f'Primary diagonal: {", ".join(list(map(str,main_diagonal)))}. Sum: {sum(main_diagonal)}')
print(f'Secondary diagonal: {", ".join(list(map(str,secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}')