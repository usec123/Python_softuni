n = int(input())

parking_lot = set()

for _ in range(n):
    dir, number = input().split(', ')
    
    if dir == 'IN':
        parking_lot.add(number)
    
    else:
        parking_lot.remove(number)

print('\n'.join(parking_lot) if parking_lot else 'Parking Lot is Empty')