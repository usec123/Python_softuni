stops = input()

cmd = input()
while cmd!='Travel':
    cmd = cmd.split(':')
    
    if cmd[0] == 'Add Stop':
        index = int(cmd[1])
        string = cmd[2]
        if index in range(len(stops)):
            stops = stops[:index:] + string + stops[index::]
    
    elif cmd[0] == 'Remove Stop':
        start_index = int(cmd[1])
        stop_index = int(cmd[2])
        if start_index in range(len(stops)) and\
            stop_index in range(len(stops)):
            stops = stops[:start_index:] + (stops[stop_index+1::] if stop_index+1 in range(len(stops)) else '')
    
    elif cmd[0] == 'Switch':
        old_string = cmd[1]
        new_string = cmd[2]
        stops = stops.replace(old_string,new_string)
        
    print(stops)
    
    cmd = input()

print(f'Ready for world tour! Planned stops: {stops}')