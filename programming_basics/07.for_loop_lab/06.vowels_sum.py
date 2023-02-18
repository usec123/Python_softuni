word = input()
sum = 0
for x in word:
    if x=='a': sum+=1
    if x=='e': sum+=2
    if x=='i': sum+=3
    if x=='o': sum+=4
    if x=='u': sum+=5

print(sum)