cmds = input().split('#')
water = int(input())
FIRE_LOW = list(range(1,51))
FIRE_MED = list(range(51,81))
FIRE_HIGH = list(range(81,126))
effort=0
put_out = []

for cmd in cmds:
    cmdt = cmd.split(' = ')
    type = cmdt[0]
    value = int(cmdt[1])
    if (type == 'Low' and value in FIRE_LOW) or (type == 'Medium' and value in FIRE_MED) or (type == 'High' and value in FIRE_HIGH):
        if value <= water:
            water-=value
            effort += value/4
            put_out.append(value)

print('Cells:')
for num in put_out: print(f' - {num}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(put_out)}')