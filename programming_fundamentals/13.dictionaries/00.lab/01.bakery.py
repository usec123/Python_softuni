items = input().split()
bakery = {items[x]:int(items[x+1]) for x in range(0,len(items),2)}
print(bakery)