qty_of_decorations = int(input())
days_left_until_christmas = int(input())
christmas_spirit = 0
price = 0
for x in range(1,days_left_until_christmas+1):
    if x%11 == 0: qty_of_decorations+=2
    if x%2==0:
        price += qty_of_decorations*2
        christmas_spirit += 5
    if x%3==0:
        price += qty_of_decorations*5 + qty_of_decorations*3
        christmas_spirit += 3 + 10
    if x%5==0:
        price += qty_of_decorations*15
        christmas_spirit += 17
        if x%3==0:
            christmas_spirit += 30
    if x%10 == 0:
        christmas_spirit -= 20
        price += 5 + 3 + 15
if days_left_until_christmas % 10 == 0: christmas_spirit -= 30
print(f'Total cost: {price}')
print(f'Total spirit: {christmas_spirit}')