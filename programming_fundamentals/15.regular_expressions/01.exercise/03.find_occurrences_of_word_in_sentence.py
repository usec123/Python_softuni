import re
sentence = input()
word_to_find = input()
print(len(re.findall(rf'\b{word_to_find}\b',sentence,re.IGNORECASE)))