def logged(function):
    def wrapper(*args):
        params = ', '.join([str(item) for item in args])
        return (
            f'you called {function.__name__}({params})\n'
            f'it returned {function(*args)}'
        )
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))
