def rectangle(len, width):
    def area(len,width):
        return len*width

    def perimeter(len,width):
        return 2*len + 2*width
    
    if not (type(len) == int and type(width) == int):
        return "Enter valid values!"
    return f'Rectangle area: {area(len,width)}\nRectangle perimeter: {perimeter(len,width)}'

print(rectangle(2, 10))
print(rectangle('2', 10))