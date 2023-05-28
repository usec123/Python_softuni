nums = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    nums.remove(min(nums))

print(', '.join(str(num) for num in nums))