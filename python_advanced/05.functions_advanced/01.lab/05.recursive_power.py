def recursive_power(number, power, new_number = 1):
    if power == 0:
        return new_number
    return recursive_power(number, power-1, new_number*number)

print(recursive_power(2,10))
print(recursive_power(10,100))