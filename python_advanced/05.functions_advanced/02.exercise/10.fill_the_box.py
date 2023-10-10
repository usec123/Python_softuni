def fill_the_box(height, lenght, width, *args):
    volume_left = height * lenght * width
    needed = 0
    full = False
    for x in args:
        if x == 'Finish':
            break
        volume_left -= x
    if volume_left < 0:
        needed = -volume_left
    if needed > 0:
        return f'No more free space! You have {needed} more cubes.'
    return f'There is free space in the box. You could put {volume_left} more cubes.'

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))