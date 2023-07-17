import re

participants = input().split(', ')

distances = {}

pattern = r'([a-zA-Z])|(\d)'
cmd = input()
while cmd!='end of race':
    info = re.findall(pattern,cmd)
    name = ''.join([x[0] for x in info])
    distance = sum([int(y) for y in ''.join([x[1] for x in info if x != ''])])
    if name in participants:
        if name in distances:
            distances[name]+=distance
        else:
            distances[name] = distance
    cmd = input()
sorted_distances = {key:value for key,value in sorted(distances.items(),key= lambda x: -x[1])}
keys = list(sorted_distances.keys())
print(f'1st place: {keys[0]}')
print(f'2nd place: {keys[1]}')
print(f'3rd place: {keys[2]}')