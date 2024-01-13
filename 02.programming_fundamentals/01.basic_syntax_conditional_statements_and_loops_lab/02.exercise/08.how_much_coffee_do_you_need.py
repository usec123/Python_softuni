cmd = input()
coffees_needed = 0
EVENTS = ['coding', 'dog', 'cat', 'movie']
while cmd != "END":
    if cmd in EVENTS: coffees_needed += 1
    elif cmd.lower() in EVENTS: coffees_needed += 2
    cmd = input()
if coffees_needed > 5: print('You need extra sleep')
else: print(coffees_needed)