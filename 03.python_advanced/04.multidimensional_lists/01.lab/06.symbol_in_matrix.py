size = int(input())

matrix = []

for _ in range(size):
    matrix.append([char for char in input()[:size:]])

symbol = input()

found = False

for x in range(size):
    if symbol in matrix[x]:
        found = True
        print(f'({x}, {matrix[x].index(symbol)})')
        break

if not found:
    print(f'{symbol} does not occur in the matrix')