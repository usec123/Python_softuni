from collections import deque
food_qty = int(input())
orders = deque(list(map(int,input().split())))
print(max(orders))

while len(orders) > 0:
    current = orders.popleft()
    if food_qty >= current:
        food_qty -= current
    
    else:
        orders.appendleft(current)
        break

if len(orders) == 0:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join([str(item) for item in orders])}')