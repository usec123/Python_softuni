from math import inf

rows,cols = list(map(int,input().split()))

matrix = [list(map(int,input().split()[:cols:])) for _ in range(rows)]

max_sum = -inf
max_coords = [0,0]

for x in range(rows-2):
    for y in range(cols-2):
        current_sum = sum([
            matrix[x+a][y+b] for a in range(3) for b in range(3)
            ])
        if current_sum > max_sum:
            max_sum = current_sum
            max_coords = [x,y]
            

print(f'Sum = {max_sum}')
print('\n'.join([' '.join([str(item) for item in row[max_coords[1]:max_coords[1]+3]]) for row in matrix[max_coords[0]:max_coords[0]+3]]))
