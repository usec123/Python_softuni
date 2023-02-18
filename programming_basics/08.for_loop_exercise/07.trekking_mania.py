musalla = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

total = 0

groups = int(input())
for _ in range(groups):
    people = int(input())
    total += people
    if people <= 5: musalla += people
    elif people <= 12: montblanc += people
    elif people <= 25: kilimanjaro += people
    elif people <= 40: k2+=people
    else: everest+=people
print(f'{musalla/total*100:.2f}%')
print(f'{montblanc/total*100:.2f}%')
print(f'{kilimanjaro/total*100:.2f}%')
print(f'{k2/total*100:.2f}%')
print(f'{everest/total*100:.2f}%')