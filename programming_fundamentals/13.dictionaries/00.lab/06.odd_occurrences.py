words = input().lower().split()

count = {}
for x in words:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1

for (key,value) in count.items():
    if value%2==1:
        print(f'{key} ',end='')