from collections import deque

text = input().split(';')

robot_dict = {item.split('-')[0]:item.split('-')[1] for item in text}

robot_timers_dict = {name:0 for name in robot_dict.keys()}

starting_time = list(map(int,input().split(':')))

products = deque()

cmd = input()
while cmd!='End':
    products.append(cmd)
    cmd = input()

while len(products) > 0:
    starting_time[2] += 1
    if starting_time[2] == 60:
        starting_time[2] = 0
        starting_time[1] += 1
    if starting_time[1] == 60:
        starting_time[1] = 0
        starting_time[0] += 1
    if starting_time[0] == 24:
        starting_time[0] = 0
    
    for key in robot_timers_dict.keys():
        if robot_timers_dict[key]!=0:
            robot_timers_dict[key]-=1
    
    taken = False
    for x in robot_dict.keys():
        if robot_timers_dict[x]==0:
            robot_timers_dict[x]=int(robot_dict[x])
            print(f'{x} - {products.popleft()} [{":".join([f"{item:02d}" for item in starting_time])}]')
            taken = True
            break
    
    if not taken:
        products.append(products.popleft())