text = input()

chars = {}

for x in text:
    if x not in chars:
        chars[x] = 0
    chars[x] += 1

chars = dict(sorted(chars.items()))

for key,value in chars.items():
    print(f'{key}: {value} time/s')