a = int(input())
b = int(input())
print(f'Before:\na = {a}\nb = {b}')
x = a
a = b
b = x
print(f'After:\na = {a}\nb = {b}')