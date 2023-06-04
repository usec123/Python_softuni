def division_of_factorials(a:int, b:int)->float:
    return f'{(fact(a)/fact(b)):.2f}'

def fact(num:int)->int:
    multiplication = 1
    for x in range(1,num+1):
        multiplication*=x
    return multiplication

print(division_of_factorials(int(input()),int(input())))