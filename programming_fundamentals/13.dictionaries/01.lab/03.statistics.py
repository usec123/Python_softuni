cmd = input()
items = {}
while cmd!='statistics':
    cmd = cmd.split(': ')
    if cmd[0] not in items.keys():
        items[cmd[0]] = int(cmd[1])
    else:
        items[cmd[0]] += int(cmd[1])
    cmd = input()
print('Products in stock:')
for x in items.keys():
    print(f'- {x}: {items[x]}')
print(f'Total Products: {len(items.keys())}')
print(f'Total Quantity: {sum(items.values())}')