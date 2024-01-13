'''
"Shadowmourne" - requires 250 Shards
"Valanyr" - requires 250 Fragments
"Dragonwrath" - requires 250 Motes
'''

items = {'shards':0,'fragments':0,'motes':0}

legendary_items = {'shards':'Shadowmourne','fragments':'Valanyr','motes':'Dragonwrath'}

while max([items['shards'], items['fragments'], items['motes']])<250:
    new_items = input().split()
    for _ in range(0,len(new_items),2):
        qty = int(new_items[0])
        material = new_items[1].lower()
        for _ in range(2):
            new_items.pop(0)
        if material in items.keys():
            items[material] += qty
        else:
            items[material] = qty
        if max([items['shards'], items['fragments'], items['motes']])>=250:
            break

for item in ['shards','fragments','motes']:
    if items[item] >= 250:
        max_item = item
        items[item] -= 250
        break

print(f'{legendary_items[max_item]} obtained!')
for key,value in items.items():
    print(f'{key}: {value}')