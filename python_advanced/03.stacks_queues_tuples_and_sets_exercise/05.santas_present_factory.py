from collections import deque

PRESENT_MAGIC = {
    150:'Doll',
    250:'Wooden train',
    300:'Teddy bear',
    400:'Bicycle'
}

materials = list(map(int,input().split()))
magic_level = deque(map(int,input().split()))

crafted_presents = {}

while materials and magic_level:
    
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()
    
    total_magic_level = current_material*current_magic_level
    
    if total_magic_level in PRESENT_MAGIC:
        if PRESENT_MAGIC[total_magic_level] in crafted_presents:
            crafted_presents[PRESENT_MAGIC[total_magic_level]] += 1
        else:
            crafted_presents[PRESENT_MAGIC[total_magic_level]] = 1
    
    else:
        if total_magic_level < 0:
            materials.append(current_material+current_magic_level)
        elif total_magic_level > 0:
            materials.append(current_material+15)
        else:
            if current_material != 0:
                materials.append(current_material)
            if current_magic_level != 0:
                magic_level.appendleft(current_magic_level)

if ('Doll' in crafted_presents and 'Train' in crafted_presents) or\
        ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
        print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
    
if materials:
    print(f'Materials left: {", ".join(list(map(str,materials))[::-1])}')
if magic_level:
    print(f'Magic left: {", ".join(list(map(str,magic_level)))}')

for key,value in dict(sorted(crafted_presents.items())).items():
    print(f'{key}: {value}')
