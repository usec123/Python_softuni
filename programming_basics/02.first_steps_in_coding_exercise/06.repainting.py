nylon_price = 1.5
dye_price = 14.5
dilute_price = 5

nylon_amount = int(input())
dye_amount = int(input())
dilute_amount = int(input())
hours = int(input())

dye_amount *= 1.1
nylon_amount += 2
bags = 0.4

material_price = (nylon_amount*nylon_price)+\
    (dye_amount*dye_price)+\
    (dilute_amount*dilute_price)+bags
hourlyPay = 0.3*material_price

total = material_price + hourlyPay*hours
print(total)