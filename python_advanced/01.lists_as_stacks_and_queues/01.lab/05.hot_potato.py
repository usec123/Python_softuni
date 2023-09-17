names = input().split()
nth_toss = int(input())

index = -1

while len(names) > 1:
    index = (index+nth_toss)%len(names)
    print(f'Removed {names.pop(index)}')
    index-=1

print(f'Last is {names[0]}')