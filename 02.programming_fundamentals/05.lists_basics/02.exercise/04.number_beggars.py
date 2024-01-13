nums = list(map(int,input().split(', ')))
beggars = int(input())
while len(nums) < beggars: nums.append(0)
output = []
for num in range(beggars):
    output.append(sum(nums[num::beggars]))
print(output)