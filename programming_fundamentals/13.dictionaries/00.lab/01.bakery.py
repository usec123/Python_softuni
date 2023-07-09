items = input().split()
bakery = {}
for x in range(0, len(items),2):
    bakery[items[x]] = int(items[x+1])
print(bakery)