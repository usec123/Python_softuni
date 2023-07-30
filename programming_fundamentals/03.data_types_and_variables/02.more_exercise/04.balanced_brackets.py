n = int(input())
opened_bracket = False
balanced = True
for x in range(n):
    inp = input()
    if inp == '(':
        if opened_bracket:
            balanced = False
        else:
            opened_bracket = True
    elif inp == ')':
        if opened_bracket:
            opened_bracket=False
        else:
            balanced = False
print('BALANCED' if balanced else 'UNBALANCED')