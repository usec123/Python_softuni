number_of_orders = int(input())
price_total = 0
for x in range(number_of_orders):
    cont = False
    price_per_capsule = float(input())
    if not 0.01<=price_per_capsule<=100: cont = True
    days = int(input())
    if not 0<days<32: cont = True
    capsules_per_day = int(input())
    if not 0<capsules_per_day<2001: cont = True
    if cont: continue
    price_order = capsules_per_day * days * price_per_capsule
    print(f'The price for the coffee is: ${price_order:.2f}')
    price_total += price_order
print(f'Total: ${price_total:.2f}')