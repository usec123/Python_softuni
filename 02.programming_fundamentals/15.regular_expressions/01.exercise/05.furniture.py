import re
cmd = input()
pattern = r'>>(\w+)<<(\d+|\d+.\d+)!(\d+)'
total = 0
print('Bought furniture:')
while cmd!='Purchase':
    result = re.search(pattern,cmd)
    if result:
        print(result.group(1))
        total+=float(result.group(2)) * int(result.group(3))
    cmd = input()

print(f'Total money spend: {total:.2f}')