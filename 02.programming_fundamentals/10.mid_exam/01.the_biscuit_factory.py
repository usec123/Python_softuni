from math import floor

biscuits_per_day = int(input())
workers = int(input())
biscuits_competitor = int(input())

DAYS = 30

biscuits = 0

made_biscuits = biscuits_per_day*workers

for x in range(1, DAYS+1):
    if x%3==0:
        biscuits+=floor(made_biscuits*0.75)
    else:
        biscuits+=made_biscuits

print(f'You have produced {biscuits} biscuits for the past month.')
print(f'You produce {((biscuits-biscuits_competitor)/biscuits_competitor*100):.2f} percent more biscuits.')\
    if biscuits > biscuits_competitor else\
print(f'You produce {((biscuits_competitor-biscuits)/biscuits_competitor*100):.2f} percent less biscuits.')