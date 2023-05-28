l = ['a', {'pi':3.14}]
print(l[1]['pi'])

empty_list = list() #same as []

inp = '1 2 3'
split_list = list(map(int, inp.split(' ')))
print(split_list)

#str.join only works on string lists
print(' | '.join([str(num) for num in split_list]))

error_list = ['a', 'b', 'c']
try:
    print(error_list[100])
except ValueError:
    print('valueerror')