energy = int(input())

cmd = input()
battles_won = 0
enough_energy = True

while cmd!='End of battle':
    cmd = int(cmd)
    if cmd > energy:
        enough_energy = False
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        break
    energy -= cmd
    battles_won += 1
    if battles_won%3==0:
        energy+=battles_won
    cmd = input()
        
if enough_energy:
    print(f'Won battles: {battles_won}. Energy left: {energy}')