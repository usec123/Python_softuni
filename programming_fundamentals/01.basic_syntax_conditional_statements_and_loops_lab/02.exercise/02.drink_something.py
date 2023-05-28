KID_AGE = 14
TEEN_AGE = 18
YOUNG_ADULT_AGE = 21

age = int(input())
if age <= KID_AGE: print('drink toddy')
elif age <= TEEN_AGE: print('drink coke')
elif age <= YOUNG_ADULT_AGE: print('drink beer')
else: print('drink whisky')