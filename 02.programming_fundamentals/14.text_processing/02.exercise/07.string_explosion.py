text = input().split('>')

new_text = [text[0]]
leftover = 0

for x in text[1::]:
    num = int(x[0])
    leftover+=num
    while leftover>0 and len(x) > 0:
        x=x[1::]
        leftover-=1
    new_text.append(x)

print('>'.join(new_text))