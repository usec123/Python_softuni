n = int(input())
synonyms = {}

for _ in range(n):
    key = input()
    value = input()
    if key in synonyms.keys():
        synonyms[key].append(value)
    else:
        synonyms[key] = [value]

for key,value in synonyms.items():
    print(f'{key} - {", ".join(value)}')