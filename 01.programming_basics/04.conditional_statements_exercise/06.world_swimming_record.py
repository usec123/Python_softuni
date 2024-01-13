from math import floor

WATER_FRICTION = 12.5 # per 15m (floor)

record = float(input())
distance = float(input())
time_for_1m = float(input())

time = distance*time_for_1m + floor(distance/15)*WATER_FRICTION

if time < record: print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else: print(f'No, he failed! He was {time - record:.2f} seconds slower.')