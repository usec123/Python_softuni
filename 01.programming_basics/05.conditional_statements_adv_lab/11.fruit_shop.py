PRODUCTS = ['banana','apple','orange','grapefruit','kiwi','pineapple','grapes']
PRICES_WORK_DAYS = [2.5,1.2,.85,1.45,2.7,5.5,3.85]
PRICES_WEEKENDS = [2.7,1.25,.9,1.6,3,5.6,4.2]

fruit = input()
day = input()
amount = float(input())

if day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] and fruit in PRODUCTS: 
    if day in ['Saturday','Sunday']: price = amount*PRICES_WEEKENDS[PRODUCTS.index(fruit)]
    else: price = amount*PRICES_WORK_DAYS[PRODUCTS.index(fruit)]
    print(f'{price:.2f}')
else:print('error')