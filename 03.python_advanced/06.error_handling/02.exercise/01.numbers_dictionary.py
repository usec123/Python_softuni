numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    
    # check if input is a number and raise exception if it isn't
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
    finally:
        line = input()
    
line = input()
while line != "Remove":
    # check if searched number exists in dictionary, if not print an error message
    searched = line
    if searched not in numbers_dictionary:
        print('Number does not exist in dictionary')
    else:
        print(numbers_dictionary[searched])
    line = input()

line = input()
while line != "End":
    # check if searched number exists in dictionary, if not print an error message
    searched = line
    if searched not in numbers_dictionary:
        print('Number does not exist in dictionary')
    else:
        del numbers_dictionary[searched]
    line = input()
    
print(numbers_dictionary)