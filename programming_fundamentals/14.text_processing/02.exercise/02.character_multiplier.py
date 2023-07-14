total = 0
text1, text2 = input().split()[:2]

for x in range(max(len(text1),len(text2))):
    temp1 = 1
    temp2 = 1
    if x in range(len(text1)):
        temp1 = ord(text1[x])
    if x in range(len(text2)):
        temp2 = ord(text2[x])
    total+=temp1*temp2

print(total)