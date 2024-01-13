def calculate(operator:str,num1:int,num2:int)->int:
    return {
        'multiply': num1*num2,
        'divide':int(num1/num2),
        'add':num1+num2,
        'subtract':num1-num2
    }.get(operator, 'Invalid operator')

print(calculate(input(),int(input()),int(input())))