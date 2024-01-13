lost_fights = int(input())
HELMET_PRICE = float(input())
SWORD_PRICE = float(input())
SHIELD_PRICE = float(input())
ARMOR_PRICE = float(input())
total_price = 0
second_broken_shield = False

for x in range(1,lost_fights+1):
    if x%2==0: total_price+=HELMET_PRICE
    if x%3==0: 
        total_price+=SWORD_PRICE
        if x%2==0: 
            total_price+=SHIELD_PRICE
            if second_broken_shield:
                total_price+=ARMOR_PRICE
                second_broken_shield = False
            else: second_broken_shield = True
print(f'Gladiator expenses: {total_price:.2f} aureus')