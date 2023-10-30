# running this file alone will result in an error because of the relative path
from .operations import sum_nums,sub_nums,mult_nums,div_nums,pow_nums

mapper = {
    '+':sum_nums,
    '-':sub_nums,
    '*':mult_nums,
    '/':div_nums,
    '^':pow_nums
}

def calculate(expression:str):
    (first,sign,second) = expression.split()
    
    if sign in mapper:
        print(f'{mapper[sign](float(first),float(second)):.2f}')
    else:
        print('invalid operation')