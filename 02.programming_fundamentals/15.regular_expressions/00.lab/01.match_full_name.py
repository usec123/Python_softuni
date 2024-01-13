import re
names = input()
found_names = re.findall(r'\\b[A-Z][a-z]+ [A-Z][a-z]+\\b', names)
print(' '.join(found_names))