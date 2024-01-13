def is_even(num):
    return num%2==0

numbers = list(map(int,input().split(' ')))
print(list(filter(is_even,numbers)))