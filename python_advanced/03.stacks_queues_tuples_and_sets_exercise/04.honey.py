from collections import deque

honey = 0

working_bees = deque(map(int,input().split()))
list_nectar = list(map(int,input().split()))
process = deque(input().split())

while working_bees and list_nectar:
    bee = working_bees.popleft()
    nectar = list_nectar.pop()
    
    if nectar >= bee:
        symbol = process.popleft()
        
        result = 0
        
        if symbol == '/' and nectar == 0:
            continue
        
        # this is guaranteed to be a symbol
        exec(f'result = abs(bee {symbol} nectar)')
        
        honey += result
        
    else:
        working_bees.appendleft(bee)
        continue

print(f'Total honey made: {honey}')
if working_bees:
    print(f'Bees left: {", ".join(list(map(str,working_bees)))}')
if list_nectar:
    print(f'Nectar left: {", ".join(list(map(str,list_nectar)))}')