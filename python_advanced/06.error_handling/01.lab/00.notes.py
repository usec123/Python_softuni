# Syntax error
# When code isn't written correctly
# print('a)
#       -> missing '

# Exception
# print([1,2,3][3])
#       -> list index out of range

# for multiple errors

# try:
#    print([1,2,3][int(input())])
# except (IndexError,ValueError):
#    print('Invalid input')


# try:
#    print([1,2,3][int(input())])
# except IndexError:
#     print('Invalid index')
# except ValueError:
#     print('Invalid value')

# try:
#     int(input())
# except ValueError:
#     print('except')
# else:
#     print('else')
# finally:
#     print('finally')

try:
    int(input())
except ValueError as error:
    print(error)