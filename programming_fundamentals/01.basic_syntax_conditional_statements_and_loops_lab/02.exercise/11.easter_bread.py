budget = float(input())
price_flour_1kg = float(input())
price_eggs_1pc = price_flour_1kg * 0.75
price_milk_1l = price_flour_1kg * 1.25

'''
FOR ONE LOAF
eggs - 1 pc
flour - 1kg
milk - 0.250l
'''
spent = 0
loaves = 0
colored_eggs = 0
while True:
    spent += 0.25 * price_milk_1l
    spent += price_flour_1kg
    spent += price_eggs_1pc
    if budget - spent < 0:
        break
    else:
        budget -= spent
        spent = 0
        loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0: colored_eggs -= loaves - 2
    
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")