number_of_snowballs = int(input())
max_stats = {'weight':0,'travel_time':0,'quality':0,'value':0}
for x in range(number_of_snowballs):
    weight = int(input())
    travel_time = int(input())
    quality = int(input())
    value = (weight / travel_time) ** quality
    if value > max_stats['value']:
        max_stats['weight'] = weight
        max_stats['travel_time'] = travel_time
        max_stats['quality'] = quality
        max_stats['value'] = value
print(f"{max_stats['weight']} : {max_stats['travel_time']} = {max_stats['value']:.0f} ({max_stats['quality']})")