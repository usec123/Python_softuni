budget = float(input())
season = input()

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer': spent = 0.3
    else: spent = 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer': spent = 0.4
    else: spent = 0.8
else:
    destination = 'Europe'
    spent = 0.9
    
if destination == 'Europe' or season == 'winter':type = 'Hotel'
else: type = 'Camp'
    
print(f'Somewhere in {destination}\n{type} - {budget*spent:.2f}')