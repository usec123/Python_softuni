rows,cols = list(map(int,input().split()))

matrix = [input().split()[:cols:] for _ in range(rows)]

count = 0

for x in range(rows-1):
    for y in range(cols-1):
        if len(set([
            matrix[x+a][y+b] for a in range(2) for b in range(2)
            ])) == 1:
            count+=1

print(count)