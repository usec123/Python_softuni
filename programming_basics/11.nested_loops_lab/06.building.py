floors = int(input())
rooms = int(input())

for x in range(floors,0,-1):
    current = ''
    for y in range(rooms):
        if x == floors: current+='L'
        elif x%2==0:current+='O'
        else: current+= 'A'
        current+=f'{x}{y} '
    print(current)