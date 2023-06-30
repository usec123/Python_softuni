def to_lower_system(num,system) -> str:
    n = ''
    while num > 0:
        n+=str(num%system)
        num//=system
    return n[::-1]

cnt = 0
num = int(input())
bit = input()
for x in to_lower_system(num,2):
    if x == bit:
        cnt+=1
    
print(cnt)