import re
links = []
pattern = r'(www\.[a-zA-Z0-9-]+(\.[a-z]+)+)'

found = []
cmd = input()
while cmd:
    matches = re.findall(pattern,cmd)
    if matches:
        for x in matches:
            found.append(x[0])
    cmd = input()
print('\n'.join(found))