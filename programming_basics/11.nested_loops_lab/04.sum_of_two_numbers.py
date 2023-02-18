interval_start = int(input())
interval_end = int(input())
magic_num = int(input())

found = False
counter = 0

for x in range(interval_start, interval_end+1):
    for y in range(interval_start, interval_end+1):
        counter+=1
        if x + y == magic_num:
            print(f'Combination N:{counter} ({x} + {y} = {magic_num})')
            found = True
            break
    if found: break
if not found: print(f'{counter} combinations - neither equals {magic_num}')