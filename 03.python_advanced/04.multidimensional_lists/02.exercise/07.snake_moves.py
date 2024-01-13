from collections import deque

rows,columns = list(map(int,input().split()))
SNAKE = deque([ch for ch in input()])

matrix = [deque()]
current_snake = SNAKE.copy()

for x in range(rows*columns):
    row = x//columns
    if row == len(matrix):
        matrix.append(deque())
    if row%2==0:
        matrix[row].append(current_snake.popleft())
    else:
        matrix[row].appendleft(current_snake.popleft())
        
    if len(current_snake) == 0:
        current_snake = SNAKE.copy()

print('\n'.join([''.join(row) for row in matrix]))