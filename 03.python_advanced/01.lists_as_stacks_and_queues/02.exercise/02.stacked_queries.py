n = int(input())

stack = []

for _ in range(n):
    cmd = input()
    
    if cmd.startswith('1'):
        stack.append(int(cmd.split()[1]))
    
    elif cmd=='2' and len(stack) > 0:
        stack.pop()
    
    elif cmd=='3' and len(stack) > 0:
        print(max(stack))
    
    elif cmd=='4' and len(stack) > 0:
        print(min(stack))

while True:
    print(stack.pop(),end='')
    if len(stack) == 0: break
    print(', ',end='')