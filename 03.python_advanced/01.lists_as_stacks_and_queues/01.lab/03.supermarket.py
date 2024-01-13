from collections import deque

queue = deque()

cmd = input()
while cmd!='End':
    if cmd == 'Paid':
        while queue:
            print(queue.popleft())
    
    else:
        queue.append(cmd)
    
    cmd = input()

print(f'{len(queue)} people remaining.')