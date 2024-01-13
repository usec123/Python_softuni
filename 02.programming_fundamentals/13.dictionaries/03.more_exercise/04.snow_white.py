cmd = input()

dwarves = dict() # {name_color : physics}

while cmd!='Once upon a time':
    cmd = cmd.split(' <:> ')
    dwarf_name = cmd[0]
    dwarf_hat_color = cmd[1]
    dwarf_physics = int(cmd[2])
    
    key = f'{dwarf_name}:{dwarf_hat_color}'
    
    if key in dwarves.keys():
        if dwarves[key] < dwarf_physics:
            dwarves[key] = dwarf_physics
    else:
        dwarves[key] = dwarf_physics
    
    cmd = input()

count_per_color = {}

for dwarf in dwarves.keys():
    color = dwarf.split(':')[1]
    
    if color in count_per_color.keys():
        count_per_color[color] += 1
    else:
        count_per_color[color] = 1

dwarves = dict(sorted(dwarves.items(), key = lambda x: (-x[1],-count_per_color[x[0].split(':')[1]])))

for key, physics in dwarves.items():
    key = key.split(':')
    name = key[0]
    color = key[1]
    print(f'({color}) {name} <-> {physics}')