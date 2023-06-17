prices = []
prices_taxes = []
prices_discount = []
cmd = input()
while cmd not in ['special', 'regular']:
    prices.append(float(cmd)) if float(cmd)>=0 else print('Invalid price!')
    cmd = input()

for i in range(len(prices)):
    prices_taxes.append(prices[i]*1.2)
    prices_discount.append(prices_taxes[i]*0.9 if cmd == 'special' else prices_taxes[i])

if sum(prices) == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n\
Price without taxes: {sum(prices):.2f}$\n\
Taxes: {(sum(prices_taxes) - sum(prices)):.2f}$\n\
-----------\n\
Total price: {sum(prices_discount):.2f}$")