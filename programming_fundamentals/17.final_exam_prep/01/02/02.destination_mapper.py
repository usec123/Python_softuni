import re

locations = input()

pattern = r'([=/])([A-Z][a-zA-Z][a-zA-Z]+)\1'

valid_locations = []

for location in re.finditer(pattern,locations):
    valid_locations.append(location.group(2))

travel_points = sum([len(destination) for destination in valid_locations])

print(f'Destinations: {", ".join(valid_locations)}')
print(f'Travel Points: {travel_points}')