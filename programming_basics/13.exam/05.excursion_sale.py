SEA_PRICE = 680
MOUNTAIN_PRICE = 499

sea_excursions_amount = int(input())
mountain_excursions_amount = int(input())

cmd = input()
total = 0

sold_out = False

while cmd!='Stop':
    if cmd=='sea':
        if sea_excursions_amount!=0:
            total += SEA_PRICE
            sea_excursions_amount-=1
    else:
        if mountain_excursions_amount!=0:
            total += MOUNTAIN_PRICE
            mountain_excursions_amount-=1
    if sea_excursions_amount==0 and mountain_excursions_amount==0:
        sold_out = True
        break
        
    cmd = input()

if sold_out: print('Good job! Everything is sold.')
print(f'Profit: {total} leva.')