def sum_numbers(a:int,b:int)->int:
    return a+b

def subtract(a:int,b:int)->int:
    return a-b

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(subtract(sum_numbers(num1, num2),num3))