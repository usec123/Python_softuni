WATER_TANK_CAPACITY = 255
n = int(input())
current_amount = 0
for x in range(n):
    liters_to_add = int(input())
    if current_amount + liters_to_add > WATER_TANK_CAPACITY:
        print('Insufficient capacity!')
    else:
        current_amount+=liters_to_add
print(current_amount)