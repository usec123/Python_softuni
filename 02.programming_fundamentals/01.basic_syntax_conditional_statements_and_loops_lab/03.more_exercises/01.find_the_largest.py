num = input()
new_num = ''
while len(num) != 0:
    largest_num = 0
    for x in range(len(num)):
        temp = int(num[x])
        if temp>largest_num: largest_num = temp
    new_num += str(largest_num)
    num = num.replace(str(largest_num),'',1)
print(new_num)