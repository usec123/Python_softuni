cmd = input()

forces = {}
registered = []

while cmd!='Lumpawaroo':
    if '|' in cmd:
        cmd = cmd.split(' | ')
        force_side = cmd[0]
        force_user = cmd[1]
        if force_user in registered:
            continue
        if force_side in forces.keys():
            if force_user not in [users for users in forces.values()]:
                forces[force_side].append(force_user)
        else:
            forces[force_side] = [force_user]
        registered.append(force_user)
    
    elif '->' in cmd:
        cmd = cmd.split(' -> ')
        force_user = cmd[0]
        force_side = cmd[1]
        for force,users in forces.items():
            if force_user in users:
                users.pop(users.index(force_user))
                break
        if force_side in forces:
            forces[force_side].append(force_user)
        else:
            forces[force_side] = [force_user]
        print(f'{force_user} joins the {force_side} side!')
    
    cmd = input()

for key,value in forces.items():
    if value!=[]:
        print(f'Side: {key}, Members: {len(value)}')
        for x in value:
            print(f'! {x}')