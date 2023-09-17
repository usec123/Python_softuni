clothes = list(map(int,input().split()))
rack_capacity = int(input())

current_rack = 0
rack_count = 1

while len(clothes) > 0:
    value = clothes.pop()
    if current_rack + value > rack_capacity:
        current_rack = value
        rack_count += 1
        
    else:
        current_rack += value

print(rack_count)