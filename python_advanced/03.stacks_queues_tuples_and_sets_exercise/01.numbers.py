nums1 = set(map(int,input().split()))
nums2 = set(map(int,input().split()))

n = int(input())

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == 'Add':
        if cmd[1] == 'First':
            numbers = set(map(int,cmd[2::]))
            nums1 = nums1.union(numbers)

        else:
            numbers = set(map(int,cmd[2::]))
            nums2 = nums2.union(numbers)
    
    elif cmd[0] == 'Remove':
        if cmd[1] == 'First':
            numbers = set(map(int,cmd[2::]))
            nums1 = nums1.difference(numbers)

        else:
            numbers = set(map(int,cmd[2::]))
            nums2 = nums2.difference(numbers)
    
    else:
        print(nums1.issubset(nums2) or nums2.issubset(nums1))

print(', '.join(map(str,sorted(list(nums1)))))
print(', '.join(map(str,sorted(list(nums2)))))