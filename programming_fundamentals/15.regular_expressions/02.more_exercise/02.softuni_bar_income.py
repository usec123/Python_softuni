import re

cmd = input()
pattern = r'%([A-Z][a-z]+)%[^\|\$%\.]*<(\w+)>[^\|\$%\.]*\|(\d+)\|[^\|\$%\.0-9]*(\d+\.?\d*)\$'
total_income = 0
while cmd!='end of shift':
    matches = re.search(pattern,cmd)
    if matches:
        name = matches.group(1)
        product = matches.group(2)
        qty = int(matches.group(3))
        price = float(matches.group(4))
        print(f'{name}: {product} - {qty*price:.2f}')
        total_income+=qty*price
    cmd = input()
print(f'Total income: {total_income:.2f}')