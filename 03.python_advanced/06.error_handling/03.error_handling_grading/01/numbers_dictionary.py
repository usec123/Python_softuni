numbers_dictionary = {}

command = input()

while command != "Search":
    number_as_string = command

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        print("Cannot submit other data types as input!\n"
            "The variable number must be an integer!")

    command = input()


command = input()

while command != "Remove":
    searched = command

    try:
        print(numbers_dictionary[searched])

    except KeyError:
        print("Number does not exist in dictionary!\n"
              "Please try with a valid one!")

    command = input()


command = input()

while command != "End":
    searched = command

    try:
        del numbers_dictionary[searched]

    except KeyError:
        print("Cannot delete this number! Number does not exist in dictionary!")

    command = input()


print(numbers_dictionary)