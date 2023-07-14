n = int(input())

for _ in range(n):
    text = input()
    name,age,add_to_name,add_to_age = '','',False,False
    for ch in text:
        if ch in '@|#*':
            if ch=='@':
                add_to_name = True
            elif ch == '|':
                add_to_name = False
            elif ch=='#':
                add_to_age = True
            elif ch=='*':
                add_to_age = False
        else:
            if add_to_name:
                name+=ch
            elif add_to_age:
                age+=ch
    print(f'{name} is {age} years old.')