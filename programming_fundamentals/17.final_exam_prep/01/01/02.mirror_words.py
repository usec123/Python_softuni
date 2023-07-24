import re

text = input()

pattern = r'([@#])([a-zA-Z]{2}[a-zA-Z]+)\1\1([a-zA-Z]{2}[a-zA-Z]+)\1'

mirror_word_pairs = []
valid_words = 0

for match in re.finditer(pattern,text):
    if match.group(2) == match.group(3)[::-1]:
        mirror_word_pairs.append(match.group(2))
    valid_words+=1
    
if valid_words==0:
    print('No word pairs found!')
else:
    print(f'{valid_words} word pairs found!')

if len(mirror_word_pairs) == 0:
    print('No mirror words!')
else:
    print(f'The mirror words are:\n{", ".join([f"{word} <=> {word[::-1]}" for word in mirror_word_pairs])}')