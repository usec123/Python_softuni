text = input().replace(' ','')

letters = {}
for ch in text:
    if ch in letters.keys():
        letters[ch]+=1
    else:
        letters[ch]=1

for key,value in letters.items():
    print(f'{key} -> {value}')