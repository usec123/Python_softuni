from math import floor
played = int(input())
starting_points = int(input())
points = 0
won = 0

for _ in range(played):
    stage = input()
    if stage=='W': 
        won+=1
        points+=2000
    if stage=='F': points+=1200
    if stage=='SF': points+=720

print(f'Final points: {starting_points+points}')
print(f'Average points: {floor(points/played)}')
print(f'{won/played*100:.2f}%')