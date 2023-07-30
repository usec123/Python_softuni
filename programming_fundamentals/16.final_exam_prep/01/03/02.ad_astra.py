import re

text = input()

pattern = r'([|#])([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

calories = 0

matches = re.finditer(pattern,text)

for match in matches:
    calories+=int(match.group(4))

matches = re.finditer(pattern,text)

print(f'You have food to last you for: {calories//2000} days!')
for match in matches:
    print(f'Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}')