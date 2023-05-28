n = int(input())
word = input()
text_all = []
text_containing_word = []

for _ in range(n):
    text = input()
    if word in text: text_containing_word.append(text)
    text_all.append(text)
print(text_all)
print(text_containing_word)