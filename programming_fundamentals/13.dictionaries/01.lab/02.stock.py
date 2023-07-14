inp = input().split()
products = {}
for x in range(0,len(inp),2):
    products[inp[x]] = int(inp[x+1])

search = input().split()
for item in search:
    if item in products.keys():
        if products[item] == 0:
            print(f'Sorry, we don\'t have {item}')
        else:
            print(f'We have {products[item]} of {item} left')
    else:
        print(f'Sorry, we don\'t have {item}')