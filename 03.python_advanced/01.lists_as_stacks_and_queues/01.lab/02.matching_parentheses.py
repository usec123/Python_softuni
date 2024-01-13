text = input()

parenthesis = []

for x in range(len(text)):
    if text[x] == '(':
        parenthesis.append(x)
    elif text[x] == ')':
        print(text[parenthesis.pop():x+1])