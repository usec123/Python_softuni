items = list(map(float,input().split(', ')))
entry = int(input())
type_of_items = input()

items_left = items[:entry:]
items_right = items[entry+1::]

if type_of_items == 'cheap':
    items_left = [item for item in items_left if item<items[entry]]
    items_right = [item for item in items_right if item<items[entry]]

else:
    items_left = [item for item in items_left if item>=items[entry]]
    items_right = [item for item in items_right if item>=items[entry]]

dmg_left = int(sum(items_left))
dmg_right = int(sum(items_right))

print(f'Right - {dmg_right}' if dmg_right>dmg_left else f'Left - {dmg_left}')