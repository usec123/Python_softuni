from collections import deque

chocolates = list(map(int,input().split(', ')))
milk = deque(map(int,input().split(', ')))

milkshakes_prepared = 0

def get_products():
    if not chocolates or not milk:
        return False,None
    
    current_chocolate = chocolates.pop()
    current_milk = milk.popleft()
    
    while current_chocolate <= 0 and current_milk <= 0:
        if not chocolates or not milk:
            return False, None
        current_chocolate = chocolates.pop()
        current_milk = milk.popleft()
    
    while current_chocolate <= 0:
        if not chocolates:
            milk.appendleft(current_milk)
            return False,None
        current_chocolate = chocolates.pop()
    
    while current_milk <= 0:
        if not milk:
            chocolates.append(current_chocolate)
            return False,None
        current_milk = milk.popleft()
    
    return current_chocolate,current_milk
    

while chocolates and milk and milkshakes_prepared < 5:
    
    current_chocolate,current_milk = get_products()
    
    if not current_chocolate:
        break
    
    if current_chocolate == current_milk:
        milkshakes_prepared += 1
    
    else:
        milk.append(current_milk)
        chocolates.append(current_chocolate-5)
    
print('Great! You made all the chocolate milkshakes needed!' if milkshakes_prepared == 5 else 'Not enough milkshakes.')
print(f'Chocolate: {", ".join(list(map(str,chocolates)))}' if chocolates else 'Chocolate: empty')
print(f'Milk: {", ".join(list(map(str,milk)))}' if milk else 'Milk: empty')