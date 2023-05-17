word = input()
output = []
for x in range(len(word)):
    if word[x].isupper():
        output.append(x)
print(output)