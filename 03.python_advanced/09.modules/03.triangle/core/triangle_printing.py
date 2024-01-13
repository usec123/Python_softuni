def print_row(i):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

def print_top(n):
    for i in range(1,n+1):
        print_row(i)
    
def print_bottom(n):
    for i in range(n-1, 0, -1):
        print_row(i)

def print_triangle(n):
    print_top(n)
    print_bottom(n)