from math import ceil

GOAL_KM = 1000

days = int(input())
current_distance = float(input())

total_distance = current_distance

for x in range(days):
    increase = int(input())/100 # %
    current_distance += current_distance*increase
    total_distance += current_distance

if total_distance>=1000: print(f"You've done a great job running {ceil(total_distance-GOAL_KM)} more kilometers!")
else: print(f"Sorry Mrs. Ivanova, you need to run {ceil(GOAL_KM-total_distance)} more kilometers")