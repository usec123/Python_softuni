text = input()
print('\n'.join([text[x]+text[x+1] for x in range(len(text)) if text[x] == ':']))