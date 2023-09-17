# QUEUE - FIFO

from collections import deque

queue = [1,2,3,4,5,6,7,8]

queue = deque(queue)
print(queue)

queue.append(9)
print(queue)

queue.appendleft(0)
print(queue)

print(queue.popleft())
print(queue)

# STACK - FILO

stack = []
stack.append(1)
print(stack)
print(stack.pop())
print(stack)