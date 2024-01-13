nums = list(map(int,input().split(', ')))
print([i for i in range(len(nums)) if nums[i]%2==0])