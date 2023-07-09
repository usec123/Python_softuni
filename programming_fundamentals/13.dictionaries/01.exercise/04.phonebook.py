cmd = input().split('-')
contacts = {}

while len(cmd)>1:
    contacts[cmd[0]] = cmd[1]
    cmd = input().split('-')

cmd = int(cmd[0])

for _ in range(cmd):
    lookup = input()
    if lookup not in contacts.keys():
        print(f'Contact {lookup} does not exist.')
    else:
        print(f'{lookup} -> {contacts[lookup]}')