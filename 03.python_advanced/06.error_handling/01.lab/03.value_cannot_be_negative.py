class ValueCannotBeNegative(Exception):
    pass

for _ in range(5):
    if float(input())<0:
        raise ValueCannotBeNegative