def sum_nums(a,b):
    return a+b

def sub_nums(a,b):
    return a-b

def mult_nums(a,b):
    return a*b

def div_nums(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    
def pow_nums(a,b):
    return a**b