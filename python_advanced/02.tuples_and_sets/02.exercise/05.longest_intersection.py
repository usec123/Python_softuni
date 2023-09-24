n = int(input())

max_len = -1
max_set = None

for _ in range(n):
    cmd = list(map(lambda x: list(map(int,x.split(','))),input().split('-')))
    cmd = [set(range(x[0],x[1]+1)) for x in cmd]
    cmd = cmd[0].intersection(cmd[1])
    if len(cmd) > max_len:
        max_len = len(cmd)
        max_set = cmd

print(f'Longest intersection is [{", ".join(list(map(str,sorted(max_set))))}] with length {max_len}')