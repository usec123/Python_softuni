age = float(input())
sex = input()

if age >= 16:
    if sex == 'm': print('Mr.')
    else: print('Ms.')
else:
    if sex=='m': print('Master')
    else: print('Miss')