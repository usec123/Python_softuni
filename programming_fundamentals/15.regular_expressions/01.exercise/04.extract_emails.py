import re
text = input()
pattern = r'\s([a-z0-9]+[a-z0-9\.\-\_]*@[a-z\-]+\.[a-z\.\-]+)\b'
print('\n'.join(re.findall(pattern,text)))