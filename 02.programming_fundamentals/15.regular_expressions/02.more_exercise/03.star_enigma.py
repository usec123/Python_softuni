import re

n = int(input())
pattern = r'@([a-zA-Z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)'
attacked_planets,destroyed_planets = [],[]
for _ in range(n):
    message = input()
    lower_value = len(re.findall(r'[star]',message,re.IGNORECASE))
    new_message = ''.join([chr(ord(x)-lower_value) for x in message])
    matches = re.search(pattern,new_message)
    if matches:
        planet = matches.group(1)
        attack_type = matches.group(3)
        if attack_type == 'A':
            attacked_planets.append(planet)
        elif attack_type == 'D':
            destroyed_planets.append(planet)

attacked_planets = sorted(attacked_planets)
destroyed_planets = sorted(destroyed_planets)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in attacked_planets: print(f'-> {planet}')

print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in destroyed_planets: print(f'-> {planet}')