text = input()
print(''.join([text[0]]+[text[x] for x in range(1,len(text)) if text[x]!=text[x-1]]))