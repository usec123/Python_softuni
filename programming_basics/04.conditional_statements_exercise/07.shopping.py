budget = float(input())
gpu_num = int(input())
cpu_num = int(input())
ram_num = int(input())

GPU_PRICE = 250
gpu_pay = GPU_PRICE*gpu_num
CPU_PRICE = 0.35*gpu_pay
cpu_pay = CPU_PRICE*cpu_num
RAM_PRICE = 0.1*gpu_pay
ram_pay = RAM_PRICE*ram_num

total = gpu_pay + cpu_pay + ram_pay

if gpu_num > cpu_num: total *= .85

if total <= budget: print(f'You have {budget-total:.2f} leva left!')
else: print(f'Not enough money! You need {total-budget:.2f} leva more!')