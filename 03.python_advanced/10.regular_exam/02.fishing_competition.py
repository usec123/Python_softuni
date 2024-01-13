fishing_area_size = int(input())

fishing_area = []
current_location = []
nums = [f'{n}' for n in range(0,10)]
collected = 0
whirlpooled = False

for n in range(fishing_area_size):
    fishing_area.append([])
    text = input()
    for ch in range(len(text)):
        fishing_area[n].append(text[ch])
        if text[ch] == 'S':
            current_location = [n,ch]

cmd = input()

while cmd!='collect the nets':
    if cmd=='up':
        fishing_area[current_location[0]][current_location[1]] = '-'
        if current_location[0] > 0:
            current_location = [current_location[0]-1, current_location[1]]
        else:
            current_location = [len(fishing_area)-1, current_location[1]]
    
    if cmd=='down':
        fishing_area[current_location[0]][current_location[1]] = '-'
        if current_location[0] < fishing_area_size - 1:
            current_location = [current_location[0]+1, current_location[1]]
        else:
            current_location = [0, current_location[1]]
    
    if cmd=='left':
        fishing_area[current_location[0]][current_location[1]] = '-'
        if current_location[1] > 0:
            current_location = [current_location[0], current_location[1]-1]
        else:
            current_location = [current_location[0], len(fishing_area[current_location[0]])-1]
    
    if cmd=='right':
        fishing_area[current_location[0]][current_location[1]] = '-'
        if current_location[1] < len(fishing_area[current_location[0]])-1:
            current_location = [current_location[0], current_location[1]+1]
        else:
            current_location = [current_location[0], 0]
    
    catch = fishing_area[current_location[0]][current_location[1]]
    
    fishing_area[current_location[0]][current_location[1]] = 'S'
    
    if catch in nums:
        collected += int(catch)
    elif catch == 'W':
        whirlpooled = True
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{current_location[0]},{current_location[1]}]')
        break
    
    cmd=input()
    
if collected >= 20:
    print('Success! You managed to reach the quota!')
elif not whirlpooled:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20-collected} tons of fish more.")
    
if collected > 0 and not whirlpooled:
    print(f"Amount of fish caught: {collected} tons.")
    
if not whirlpooled:
    print('\n'.join([''.join([a for a in row]) for row in fishing_area]))
