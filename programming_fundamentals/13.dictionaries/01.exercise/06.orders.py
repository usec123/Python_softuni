cmd = input()

products_qty = {}
products_price = {}

while cmd!='buy':
    cmd = cmd.split()
    
    products_price[cmd[0]] = float(cmd[1])
    products_qty[cmd[0]] = \
        products_qty[cmd[0]] + int(cmd[2])\
        if cmd[0] in products_qty.keys()\
        else int(cmd[2])
    
    cmd = input()

for item in products_price.keys():
    print(f'{item} -> {products_price[item]*products_qty[item]:.2f}')