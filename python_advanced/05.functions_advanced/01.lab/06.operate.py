def operate(operator, *args):
    res = 0
    if operator == '+':
        for x in args:
            res+=x
    elif operator == '-':
        res = args[0]*2
        for x in args:
            res-=x
    elif operator == '*':
        res = 1
        for x in args:
            res*=x
    elif operator == '/':
        res = pow(args[0],2)
        for x in args:
            if x!=0:
                res/=x
    return res

print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 1, 2, 3))
print(operate("/", 6, 3, 2))