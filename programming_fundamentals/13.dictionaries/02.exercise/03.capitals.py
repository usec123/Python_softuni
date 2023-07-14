countries = input().split(', ')
capitals = input().split(', ')
dictionary = {countries[x]:capitals[x] for x in range(len(countries))}

for key,value in dictionary.items():
    print(f'{key} -> {value}')