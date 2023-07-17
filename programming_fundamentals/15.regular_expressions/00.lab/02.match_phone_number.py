import re
numbers = input()
valid_numbers = re.findall(r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b',numbers)
print(', '.join(valid_numbers))