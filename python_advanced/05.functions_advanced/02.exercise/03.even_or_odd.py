def even_odd(*args):
    leftover = 0 if args[-1]=='even' else 1
    return [item for item in args[:-1:] if item%2==leftover]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))