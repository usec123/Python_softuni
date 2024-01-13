from collections import deque

fuel_quantity = list(map(int,input().split())) # take last -- initial fuel
additional_consumption_index = deque(map(int,input().split())) # take first -- consumption indexes
fuel_needed = deque(map(int,input().split())) # -- quantities

max_altitude = len(fuel_needed)

current_altitude = 1

while fuel_quantity:
    fuel = fuel_quantity.pop()
    consumption = additional_consumption_index.popleft()
    
    result = fuel-consumption
    
    if result >= fuel_needed.popleft():
        print(f'John has reached: Altitude {current_altitude}')
        current_altitude += 1
    else:
        print(f'John did not reach: Altitude {current_altitude}')
        break

if current_altitude <= max_altitude:
    print(f'John failed to reach the top.')
    print(f'Reached altitudes: {", ".join([f"Altitude {n}" for n in range(1,current_altitude)])}' if current_altitude>1 else 'John didn\'t reach any altitude.')
else:
    print(f'John has reached all the altitudes and managed to reach the top!')

