# 0 -> positive and even
n = int(input())
even = []
odd = []
positive = []
negative = []
for _ in range(n):
    num = int(input())
    if num%2==0: even.append(num)
    else: odd.append(num)
    if num>=0: positive.append(num)
    else: negative.append(num)
cmd = input()
if cmd in ['even', 'odd', 'positive', 'negative']:
    exec(f'print({cmd})')