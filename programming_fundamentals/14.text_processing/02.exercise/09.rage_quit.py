text = input().upper()
symbols = set()
current_string = ''
output = ''
last_digit_index = -1

for x in range(len(text)):
    if text[x].isdigit():
        num = text[x]
        if x+1 in range(len(text)):
            if text[x+1].isdigit():
                num+=text[x+1]
                x+=1
        output+=current_string*int(num)
        current_string=''
    else:
        current_string+=text[x]
        symbols.add(text[x])

print(f'Unique symbols used: {len(symbols)}')
print(output)