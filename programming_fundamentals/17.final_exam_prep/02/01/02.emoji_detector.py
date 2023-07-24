import re

text = input()

emoji_pattern = r'([:\*])\1([A-Z][a-z][a-z]+)\1\1'
digit_pattern = r'\d'

cool_threshold = 1
for digit in re.findall(digit_pattern,text):
    cool_threshold*=int(digit)

cool_emojis = []
emoji_count = 0
for emoji in re.finditer(emoji_pattern,text):
    emoji_count+=1
    emoji_coolness = 0
    for x in emoji.group(2):
        emoji_coolness+=ord(x)
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji.group(1)*2+emoji.group(2)+emoji.group(1)*2)

print(f'Cool threshold: {cool_threshold}')
print(f'{emoji_count} emojis found in the text. The cool ones are:')
print('\n'.join(cool_emojis))