n = int(input())

users = {}

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == 'register':
        username = cmd[1]
        license_plate = cmd[2]
        if username in users.keys():
            print(f'ERROR: already registered with plate number {users[username]}')
        else:
            users[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
    
    if cmd[0] == 'unregister':
        username = cmd[1]
        if username in users.keys():
            users.pop(username)
            print(f'{username} unregistered successfully')
        else:
            print(f'ERROR: user {username} not found')

for user,plate in users.items():
    print(f'{user} => {plate}')