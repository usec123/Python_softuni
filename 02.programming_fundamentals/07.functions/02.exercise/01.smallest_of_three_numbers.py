def smallest_number(a:int,b:int,c:int):
    if a<=b:
        if a<=c:
            return a
        return c
    elif b<=c:
        return b
    return c
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest_number(num1,num2,num3))