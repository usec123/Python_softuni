SIZE = 1 # cubic meter

width = int(input())
length = int(input())
height = int(input())

volume = width*length*height

isFull = False

cmd = input()
while cmd != 'Done':
    volume -= int(cmd)
    if volume<=0:
        isFull = True
        break
    cmd = input()

if isFull: print(f'No more free space! You need {-volume} Cubic meters more.')
else: print(f'{volume} Cubic meters left.')