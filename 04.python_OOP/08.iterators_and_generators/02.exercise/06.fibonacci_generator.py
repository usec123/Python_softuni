def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        temp = first_num + second_num
        first_num = second_num
        second_num = temp


# generator = fibonacci()
#
# for i in range(5):
#     print(next(generator))


generator = fibonacci()

for i in range(1):
    print(next(generator))
