num = int(input())
if num>1:
    is_prime = True
    for x in range(2,num):
        if num%x==0: 
            is_prime = False
            break
    print(is_prime)
else: print(False)