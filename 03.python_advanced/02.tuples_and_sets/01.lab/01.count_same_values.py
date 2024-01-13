numbers = tuple(map(float,input().split()))

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = numbers.count(num)
        print(f'{num} - {occurrences[num]} times')