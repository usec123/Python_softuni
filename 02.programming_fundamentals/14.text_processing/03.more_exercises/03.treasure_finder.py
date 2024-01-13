key = list(map(int,input().split()))
message = input()
output = []

while message != 'find':
    key_index = 0
    new_message = ''

    for char in message:
        new_message += chr(ord(char)-key[key_index])
        key_index +=1
        if key_index==len(key):
            key_index = 0

    type = ''
    coords = ''
    write_type,write_coords = False,False
    for char in new_message:
        if char in '&<>':
            if char=='&':
                write_type=not write_type
            elif char == '<':
                write_coords = True
            else:
                write_coords = False
        else:
            if write_type:
                type+=char
            elif write_coords:
                coords+=char

    output.append(f'Found {type} at {coords}')
    message = input()
print('\n'.join(output))