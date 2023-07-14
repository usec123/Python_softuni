banned_words = input().split(', ')
text = input()

for x in banned_words:
    while x in text:
        text=text.replace(x,'*'*len(x))
    
print(text)