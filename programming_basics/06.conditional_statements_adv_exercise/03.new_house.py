ROSE_PRICE = 5
DAHLIA_PRICE = 3.8
TULIP_PRICE = 2.8
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.5

flower_type = input()
flower_amount = int(input())
budget = int(input())

discount = 1

if flower_type == 'Roses':
    if flower_amount > 80: discount = 0.9
    price = ROSE_PRICE*flower_amount*discount
if flower_type == 'Dahlias':
    if flower_amount > 90: discount = 0.85
    price = DAHLIA_PRICE*flower_amount*discount
if flower_type == 'Tulips':
    if flower_amount > 80: discount = 0.85
    price = TULIP_PRICE*flower_amount*discount
if flower_type == 'Narcissus':
    if flower_amount < 120: discount = 1.15
    price = NARCISSUS_PRICE*flower_amount*discount
if flower_type == 'Gladiolus':
    if flower_amount < 80: discount = 1.2
    price = GLADIOLUS_PRICE*flower_amount*discount

if budget>=price: print(f'Hey, you have a great garden with {flower_amount} '+
f'{flower_type} and {budget - price:.2f} leva left.')
else: print(f'Not enough money, you need {price - budget:.2f} leva more.')