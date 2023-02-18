width = int(input())
length = int(input())

pieces = width * length

cmd = input()
while cmd != 'STOP':
    pieces -= int(cmd)
    if pieces<0: break
    cmd = input()

if pieces <= 0: print(f'No more cake left! You need {-pieces} pieces more.')
else: print(f'{pieces} pieces are left.')