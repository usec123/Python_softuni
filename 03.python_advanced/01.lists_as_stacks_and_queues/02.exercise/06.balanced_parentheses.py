text = input()

opening_parentheses = []

balanced = True

for x in text:
    if x in '({[':
        opening_parentheses.append(x)
        
    elif x in ')}]':
        if len(opening_parentheses) > 0:
            if (opening_parentheses[-1] == '(' and x == ')') or\
            (opening_parentheses[-1] == '[' and x == ']') or\
            (opening_parentheses[-1] == '{' and x == '}'):
                opening_parentheses.pop(-1)
            else:
                balanced = False
                break
        
        else:
            balanced = False
            break
    
print('YES' if balanced else 'NO')