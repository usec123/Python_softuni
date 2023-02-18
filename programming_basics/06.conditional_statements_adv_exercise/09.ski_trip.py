ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

days = int(input())
type = input()
vote = input()

discount = 1

if type == 'apartment':
    price = APARTMENT
    if days < 10: discount = 0.7
    elif days < 15: discount = 0.65
    else: discount = 0.5
elif type == 'president apartment':
    price = PRESIDENT_APARTMENT
    if days < 10: discount = 0.9
    elif days < 15: discount = 0.85
    else: discount = 0.8
else: price = ROOM_FOR_ONE_PERSON
price *= days-1
price *= discount

if vote == 'positive':price*=1.25
else: price *= 0.9

print(f'{price:.2f}')