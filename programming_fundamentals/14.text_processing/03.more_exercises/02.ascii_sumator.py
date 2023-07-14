first = ord(input())
second = ord(input())
if first>second: first,second = second,first
text = input()
print(sum([ord(x) for x in text if ord(x) in range(first+1,second)]))