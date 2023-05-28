cmd = input().split('|')
budget = float(input())
original_budget = budget
TICKET_PRICE = 150
MAX_PRICE_CLOTHES = 50
MAX_PRICE_SHOES = 35
MAX_PRICE_ACCESSORIES = 20.5
new_prices = []

for i in cmd:
    i = i.split('->')
    item = i[0]
    price = float(i[1])
    if ((item == 'Clothes' and price <= MAX_PRICE_CLOTHES) or (item == 'Shoes' and price <= MAX_PRICE_SHOES) or (item == 'Accessories' and price <= MAX_PRICE_ACCESSORIES)) and price <= budget:
        budget-=price
        new_prices.append(price*1.4)
print(' '.join(f'{new_price:.2f}' for new_price in new_prices))
budget+=sum(new_prices)
print(f'Profit: {budget-original_budget:.2f}')
print('Hello, France!') if budget>=TICKET_PRICE else print('Not enough money.')