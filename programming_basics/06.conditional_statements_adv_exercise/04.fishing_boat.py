budget = int(input())
season = input()
amount = int(input())

total = 0

if (season == 'Spring'): total = 3000
elif (season == 'Summer' or season == 'Autumn'): total = 4200
elif (season == 'Winter'): total = 2600

discount = 1
if amount <= 6: discount = 0.9
elif amount <= 11: discount = 0.85
else: discount = 0.75

price = total * discount

if (amount%2 == 0 and season != 'Autumn'): price *= 0.95

if (budget >= price): print(f'Yes! You have {budget - price:.2f} leva left.')
else: print(f'Not enough money! You need {price - budget:.2f} leva.')