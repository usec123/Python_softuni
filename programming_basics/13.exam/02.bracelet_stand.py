DAYS = 5

pocket_money_per_day = float(input())
money_earned_per_day = float(input())
total_expenses = float(input())
price = float(input())

total_earned = (pocket_money_per_day+money_earned_per_day)*DAYS - total_expenses

if total_earned>=price:
    print(f'Profit: {total_earned:.2f} BGN, the gift has been purchased.')
else: print(f'Insufficient money: {price-total_earned:.2f} BGN.')