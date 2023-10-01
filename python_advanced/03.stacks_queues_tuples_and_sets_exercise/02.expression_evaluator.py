from collections import deque

expression = input().split()

numbers_queue = deque()

result = int(expression[0])

for x in expression[1::]:
    if x.isdigit() or (x[0]=='-' and x[1::].isdigit()):
        numbers_queue.append(int(x))
    
    else:
        while numbers_queue:
            if x == '+':
                result += numbers_queue.popleft()
            
            elif x == '-':
                result -= numbers_queue.popleft()
            
            elif x == '*':
                result *= numbers_queue.popleft()
            
            else:
                result = result//numbers_queue.popleft()
        
print(result)