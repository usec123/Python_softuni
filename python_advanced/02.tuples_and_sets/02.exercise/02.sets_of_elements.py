n, m = list(map(int,input().split()))

n_set = set()
result = set()

for _ in range(n):
    n_set.add(int(input()))
    
for _ in range(m):
    num = int(input())
    if num in n_set:
        result.add(num)

print('\n'.join(list(map(str,result))))