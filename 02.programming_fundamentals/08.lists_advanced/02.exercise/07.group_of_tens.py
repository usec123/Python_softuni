nums = list(map(int,input().split(', ')))
current_num = 10
while len(nums)>0:
	numbers = [num for num in nums if num <= current_num]
	for x in numbers: nums.remove(x)
	print(f"Group of {current_num}'s: {numbers}")
	current_num+=10