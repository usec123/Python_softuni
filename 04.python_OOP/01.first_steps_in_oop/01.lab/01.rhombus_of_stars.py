size = int(input())

def print_row(size,x):
    print(' '*(size-x),end='')
    print(*['*' for _ in range(x)])

def print_top_half(size):
    for x in range(1,size+1):
        print_row(size,x)

def print_bottom_half(size):
    for x in range(size-1,0,-1):
        print_row(size,x)
        
def print_rhombus(size):
    print_top_half(size)
    print_bottom_half(size)

print_rhombus(size)