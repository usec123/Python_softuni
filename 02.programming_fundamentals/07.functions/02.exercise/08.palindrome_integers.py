def palindrome(num:int):
    num=str(num)
    for x in range(int(len(num)/2)):
        if num[x]!=num[len(num)-1-x]:
            return False
    return True

numbers = list(map(int,input().split(', ')))
for n in numbers:
    print(palindrome(n))