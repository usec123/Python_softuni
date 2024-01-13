# def sum_nums(a,b): # a,b -> parameters
#     return a+b
# 
# print(sum_nums(2,3)) # a,b -> arguments


# *args -> allows for any amount of arguments (result - tuple)

# a, b -> required args
# *args -> additional arguments
def sum_nums(a, b, *args):
    return a+b+sum(args)

print(sum_nums(1,2))
print(sum_nums(1,2,3,4,5))
print(sum_nums(1,2,3,4,5,6,7,8,9))

# **kwargs
def example(**kwargs):
    return kwargs

print(example(num=5,name='a',id=2))

# when using ** for dict, keys must be the same as the args

# IMPORTANT
# IN JUDGE, FUNCTION NAMES MUST BE THE SAME AS THE REQUIRED ONE