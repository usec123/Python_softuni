nums = list(map(int,input().split(' ')))
for _ in range(len(nums)):
    nums.append(-(nums.pop(0)))
print(nums)