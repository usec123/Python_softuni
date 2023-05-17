age = int(input())
price = float(input())
sell_price = int(input())

sum = 0
current_amount = 10
for x in range(0,age):
    if x%2==0: sum+=sell_price
    else: 
        sum += current_amount - 1
        current_amount += 10
if sum >= price: print(f'Yes! {sum-price:.2f}')
else: print(f'No! {price-sum:.2f}')