a = int(input())
b = int(input())
operator = input()

if operator != '/' and operator != '%':
    if operator == '+': tot = a+b
    if operator == '-': tot = a-b
    if operator == '*': tot = a*b
    print(f'{a} {operator} {b} = {tot} - {"even" if tot%2==0 else "odd"}')
elif b == 0: print(f'Cannot divide {a} by zero')
else:
    if operator == '/': print(f'{a} / {b} = {a/b:.2f}')
    else: print(f'{a} % {b} = {a%b}')