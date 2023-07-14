companies = {}

cmd = input()

while cmd!='End':
    cmd = cmd.split(' -> ')
    company = cmd[0]
    id = cmd[1]
    
    if company in companies.keys():
        if id not in companies[company]:
            companies[company].append(id)
    else:
        companies[company] = [id]
    cmd = input()

for cmp,ids in companies.items():
    print(f'{cmp}')
    for id in ids:
        print(f'-- {id}')