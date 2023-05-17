ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

# <10d  >=10and<=15 >15
# DISCOUNTS_ROOM_FOR_ONE_PERSON - none
DISCOUNTS_APARTMENT = [0.3,0.35,0.5]
DISCOUNTS_PRESIDENT_APARTMENT = [0.1,0.15,0.2]

days = int(input())
type = input() # "room for one person",  "apartment" или "president apartment"
vote = input() # "positive"  или "negative"

nights = days-1

additional_charges = 0 # %

if vote == 'positive': additional_charges = 0.25
else: additional_charges = -0.1

if days < 10: index = 0
elif days < 16: index = 1
else: index = 2

discount = 0
total = 0

if type == 'room for one person':
    total = ROOM_FOR_ONE_PERSON
if type == 'apartment':
    discount = DISCOUNTS_APARTMENT[index]
    total = APARTMENT
if type == 'president apartment':
    discount = DISCOUNTS_PRESIDENT_APARTMENT[index]
    total = PRESIDENT_APARTMENT

total -= total*discount
total += total*additional_charges
total *= nights

print(f'{total:.2f}')