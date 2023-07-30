import re

pattern = r'[@#]+([a-z]{2}[a-z]+)[@#]+[^a-zA-Z0-9]*/+(\d+)/+'

text = input()

matches = re.finditer(pattern,text)

for match in matches:
    print(f'You found {match.group(2)} {match.group(1)} eggs!')