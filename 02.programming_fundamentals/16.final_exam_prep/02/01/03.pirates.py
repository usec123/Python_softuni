cmd = input()

population_dict = {}
gold_dict = {}
while cmd!='Sail':
    cmd = cmd.split('||')
    city = cmd[0]
    population = int(cmd[1])
    gold = int(cmd[2])
    if city in population_dict:
        population_dict[city] += population
        gold_dict[city] += gold
    else:
        population_dict[city] = population
        gold_dict[city] = gold
        
    cmd = input()

cmd = input()
while cmd!='End':
    cmd = cmd.split('=>')
    
    if cmd[0]=='Plunder':
        town = cmd[1]
        people = int(cmd[2])
        gold = int(cmd[3])
        if town in population_dict:
            population_dict[town] -= people
            gold_dict[town] -= gold
            print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
            if population_dict[town] <= 0 or gold_dict[town] <= 0:
                print(f'{town} has been wiped off the map!')
                population_dict.pop(town)
                gold_dict.pop(town)
    
    elif cmd[0]=='Prosper':
        town = cmd[1]
        gold = int(cmd[2])
        if town in gold_dict:
            if gold<0:
                print('Gold added cannot be a negative number!')
            else:
                gold_dict[town] += gold
                print(f'{gold} gold added to the city treasury. {town} now has {gold_dict[town]} gold.')
    
    cmd = input()

if len(list(population_dict.keys())) == 0:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(list(population_dict.keys()))} wealthy settlements to go to:')
    for key in population_dict.keys():
        print(f'{key} -> Population: {population_dict[key]} citizens, Gold: {gold_dict[key]} kg')