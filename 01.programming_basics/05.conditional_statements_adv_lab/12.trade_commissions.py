SOFIA = [0.05, 0.07, 0.08, 0.12]
VARNA = [0.045,0.075,0.1,0.13]
PLOVDIV = [0.055,0.08,0.12,0.145]
valid = True

city = input()
sales_volume = float(input())

index = 0

if sales_volume<0: valid = False
elif sales_volume <= 500: index = 0
elif sales_volume <= 1000: index = 1
elif sales_volume <= 10000: index = 2
else: index = 3

if city == 'Sofia': comm = round(sales_volume*SOFIA[index],2)
elif city == 'Varna': comm = round(sales_volume*VARNA[index],2)
elif city == 'Plovdiv': comm = round(sales_volume*PLOVDIV[index],2)
else: valid = False

if(valid): print(f'{comm:.2f}')
else: print('error')