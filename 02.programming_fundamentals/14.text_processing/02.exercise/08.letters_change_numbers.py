text = input().split()
total = 0
for x in text:
    first_letter = x[0]
    num = int(x[1:-1])
    second_letter = x[-1]

    if first_letter.islower():
        num*=ord(first_letter)-ord('a')+1

    else:
        num/=ord(first_letter)-ord('A')+1

    if second_letter.islower():
        num+=ord(second_letter)-ord('a')+1

    else:
        num-=ord(second_letter)-ord('A')+1

    total+=num

print(f'{total:.2f}')