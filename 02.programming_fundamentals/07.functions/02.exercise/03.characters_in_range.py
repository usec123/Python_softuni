def chars_in_range(char1:str, char2:str):
    char1 = ord(char1)+1
    char2 = ord(char2)
    output = ''
    for x in range(char1,char2):
        output += chr(x) + ' '
    return output
print(chars_in_range(input(),input()))