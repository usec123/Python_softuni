# [studio , apartment]

MAY_OCTOBER_PRICES = [50,65]
JUNE_SEPTEMBER_PRICES = [75.2,68.7]
JULY_AUGUST_PRICES = [76,77]

month = input()
nights = int(input())

if month in ['May','October']: prices = MAY_OCTOBER_PRICES
elif month in ['June', 'September']: prices = JUNE_SEPTEMBER_PRICES
else: prices = JULY_AUGUST_PRICES

discounts = [1,1]

if nights > 7 and (month == 'May' or month == 'October'):
    discounts[0] = 0.95
    if nights > 14: discounts[0] = 0.7
if nights > 14 and (month == 'June' or month == 'September'):discounts[0] = 0.8
if nights > 14: discounts[1] = 0.9

print(f'Apartment: {prices[1]*discounts[1]*nights:.2f} lv.')
print(f'Studio: {prices[0]*discounts[0]*nights:.2f} lv.')