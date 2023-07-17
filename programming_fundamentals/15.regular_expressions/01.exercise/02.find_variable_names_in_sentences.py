import re
print(','.join(re.findall(r'\b_([a-zA-Z0-9]+)\b',input())))