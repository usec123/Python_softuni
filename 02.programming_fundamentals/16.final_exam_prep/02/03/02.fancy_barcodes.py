import re

valid_barcode_pattern = r'@#+([A-Z][a-zA-Z0-9]{4}[a-zA-Z0-9]*[A-Z])@#+'
digits_pattern = r'\d'

n = int(input())
for _ in range(n):
    barcode = input()
    code = re.findall(valid_barcode_pattern,barcode)
    if code:
        code = code[0]
        digits = ''.join(re.findall(digits_pattern,code))
        print(f'Product group: {digits if digits else "00"}')
    else:
        print('Invalid barcode')