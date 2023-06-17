distances = list(map(int,input().split()))
removed_elements_counter = 0

while len(distances)>0:
    index = int(input())
    if 0<=index<len(distances):
        removed_element = distances.pop(index)
    elif index<0:
        removed_element = distances[0]
        distances[0] = distances[-1]
    else:
        removed_element = distances[-1]
        distances[-1] = distances[0]
    
    for i in range(len(distances)):
        if distances[i]<=removed_element:distances[i]+=removed_element
        else:distances[i]-=removed_element
    
    removed_elements_counter+=removed_element

print(removed_elements_counter)
distances = list(map(int,input().split()))
removed_elements_counter = 0

while len(distances)>0:
    index = int(input())
    if 0<=index<len(distances):
        removed_element = distances.pop(index)
    elif index<0:
        removed_element = distances[0]
        distances[0] = distances[-1]
    else:
        removed_element = distances[-1]
        distances[-1] = distances[0]
    
    for i in range(len(distances)):
        if distances[i]<=removed_element:distances[i]+=removed_element
        else:distances[i]-=removed_element
    
    removed_elements_counter+=removed_element

print(removed_elements_counter)