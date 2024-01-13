def sum_even_odd(num:int):
    sum_even = 0
    sum_odd = 0
    num = str(num)
    for char in num:
        char = int(char)
        if char%2==0:sum_even+=char
        else: sum_odd+=char
    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'

print(sum_even_odd(int(input())))