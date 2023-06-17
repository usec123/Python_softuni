def rec(x,y,last):
    coords = [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]
    if last == 'l': coords.remove([x+1,y])
    elif last == 'r': coords.remove([x-1,y])
    elif last == 'u': coords.remove([x,y-1])
    elif last == 'd': coords.remove([x,y+1])
    

rows = int(input())

for x in range(rows):
    pass