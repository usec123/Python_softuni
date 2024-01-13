def age_assignment(*args,**kwargs):
    assigned_ages = {}
    for key,value in kwargs.items():
        for name in args:
            if name[0] == key:
                assigned_ages[name] = value
    result = [f'{key} is {value} years old.' for key,value in assigned_ages.items()]
    result = sorted(result)
    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))
print('----------------------')
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))