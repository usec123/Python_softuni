budget = float(input())
extras = int(input())
price_per_extra = float(input())

decor_price = budget * 0.1
clothing_price = extras * price_per_extra
if extras>150: clothing_price*=0.9

total = decor_price + clothing_price
if total <= budget: print(f'Action!\nWingard starts filming with {budget-total:.2f} leva left.')
else: print(f'Not enough money!\nWingard needs {total-budget:.2f} leva more.')