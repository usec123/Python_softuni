cmd = input()

products = {} # prod : [qty,price]

while cmd!='buy':
    cmd = cmd.split()
    
    price = float(cmd[1])
    qty = \
        products[cmd[0]][0] + int(cmd[2])\
        if cmd[0] in products.keys()\
        else int(cmd[2])
    products[cmd[0]] = [qty,price]
    cmd = input()

for item in products.keys():
    print(f'{item} -> {products[item][1]*products[item][0]:.2f}')