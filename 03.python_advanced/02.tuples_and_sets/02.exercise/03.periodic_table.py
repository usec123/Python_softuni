n = int(input())

elements = set()

for _ in range(n):
    cmd = input().split()
    for x in cmd:
        elements.add(x)

print('\n'.join(elements))