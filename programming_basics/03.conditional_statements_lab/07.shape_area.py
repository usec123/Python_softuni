from math import *
area = 0.0
type = input()
if type == 'square':
    a = float(input())
    area = a**2
elif type == 'rectangle':
    a = float(input())
    b = float(input())
    area = a*b
elif type == 'circle':
    r = float(input())
    area = pi*(r**2)
elif type == 'triangle':
    a = float(input())
    h = float(input())
    area = a*h/2
print(f'{area:.3f}')