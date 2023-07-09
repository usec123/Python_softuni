resources = {}

while True:
    cmd = input()
    if cmd=='stop': break
    qty = int(input())
    if cmd in resources.keys():
        resources[cmd]+=qty
    else: resources[cmd] = qty
    
for key,value in resources.items():
    print(f'{key} -> {value}')