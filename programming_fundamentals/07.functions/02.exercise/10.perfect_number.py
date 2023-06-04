def perfect_number(num:int) -> str:
    sum_divisors = 0
    for x in range(1,num):
        if num%x==0:
            sum_divisors+=x
    if sum_divisors==num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

perfect_number(int(input()))