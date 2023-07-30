animal_food_dict = {}
animal_area_dict = {}
hungry_animals_area_qty = {}

cmd = input()
while cmd!='EndDay':
    cmd = cmd.split()
    
    if cmd[0] == 'Add:':
        cmd = cmd[1].split('-')
        animal_name = cmd[0]
        needed_food_qty = int(cmd[1])
        area = cmd[2]
        
        if animal_name in animal_food_dict:
            animal_food_dict[animal_name] += needed_food_qty
        else:
            animal_area_dict[animal_name] = area
            animal_food_dict[animal_name] = needed_food_qty
            if area in hungry_animals_area_qty:
                hungry_animals_area_qty[area] += 1
            else:
                hungry_animals_area_qty[area] = 1
    
    elif cmd[0] == 'Feed:':
        cmd = cmd[1].split('-')
        animal_name = cmd[0]
        food = int(cmd[1])
        
        if animal_name in animal_food_dict:
            animal_food_dict[animal_name] -= food
            if animal_food_dict[animal_name] <= 0:
                print(f'{animal_name} was successfully fed')
                animal_food_dict.pop(animal_name)
                hungry_animals_area_qty[animal_area_dict[animal_name]] -= 1
                if hungry_animals_area_qty[animal_area_dict[animal_name]] == 0:
                    hungry_animals_area_qty.pop(animal_area_dict[animal_name])
    
    cmd = input()

print('Animals:')
print('\n'.join([f' {animal} -> {food}g' for animal,food in animal_food_dict.items()]))

print('Areas with hungry animals:')
print('\n'.join([f' {key}: {value}' for key,value in hungry_animals_area_qty.items()]))