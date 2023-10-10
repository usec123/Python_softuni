from collections import deque

rows,columns = list(map(int,input().split()))
SNAKE = deque([ch for ch in input()])

matrix = []
current_snake = SNAKE
current_index = 0

while True:
    if len(matrix) == rows:
        if len(matrix[rows-1]) == columns:
            break
    
    if current_index > 1:
        matrix[current_index//columns].append(matrix[current_index//columns][-1])
        for x in range(current_index-1,0,-1):
            if x % columns != 0:
                matrix[x//columns][x%columns] = matrix[x//columns][x%columns-1]
            else:
                matrix[x//columns][x%columns] = matrix[x//columns-1][columns-1]
    
    if matrix:
        if matrix[0]:
            matrix[0][0] = current_snake.popleft()
        else:
            matrix[0].append(current_snake.popleft())
    else:
        matrix.append([])

    if len(current_snake) == 0:
        current_snake = SNAKE
    current_index += 1

print('\n'.join([' '.join(row) for row in matrix]))