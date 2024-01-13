strings = input().split()
cmd = input().split()

while cmd[0]!='3:1':
    if cmd[0] == 'merge':
        new_strings = []
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        for x in range(len(strings)):
            if start_index<x<=end_index:
                if len(new_strings) == 0: new_strings.append('')
                new_strings[-1]+=strings[x]
            else:
                new_strings.append(strings[x])
        strings = new_strings
    elif cmd[0] == 'divide':
        index = int(cmd[1])
        partitions = int(cmd[2])
        new_length = len(strings[index])//partitions
        new_strings = strings[:index:]
        to_divide = strings[index]
        text = ''
        div_counter = 1
        for x in range(len(to_divide)):
            text += to_divide[x]
            if len(text)%new_length==0 and div_counter<partitions:
                new_strings.append(text)
                text = ''
                div_counter+=1
        new_strings.append(text)
        new_strings+=strings[index+1::]
        strings = new_strings
    cmd = input().split()
    
print(' '.join(strings))