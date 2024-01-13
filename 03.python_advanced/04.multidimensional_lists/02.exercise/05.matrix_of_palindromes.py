rows,columns = list(map(int,input().split()))

matrix = [
    [f'{chr(ord("a")+y)}{chr(ord("a")+x+y)}{chr(ord("a")+y)}' for x in range(columns)] for y in range(rows)
]

print('\n'.join([' '.join(row) for row in matrix]))