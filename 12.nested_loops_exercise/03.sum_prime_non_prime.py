cmd = input()

sum_prime = 0
sum_non_prime = 0

while cmd!='stop':
    cmd = int(cmd)
    
    if cmd<0:print('Number is negative.')
    else:
        is_prime = True
        for x in range(2,cmd): 
            if cmd%x==0:
                sum_non_prime+=cmd
                is_prime = False
                break
        if is_prime: sum_prime+=cmd
    cmd = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")