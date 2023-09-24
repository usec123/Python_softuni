n = int(input())

vip = set()
guest = set()

for _ in range(n):
    code = input()
    if code[0].isdigit():
        vip.add(code)
    else:
        guest.add(code)

arrivals = set()

cmd = input()
while cmd!='END':
    arrivals.add(cmd)
    cmd = input()

missing = sorted([person for person in vip if person not in arrivals])
missing += sorted([person for person in guest if person not in arrivals])

print(len(missing))
print('\n'.join(missing))