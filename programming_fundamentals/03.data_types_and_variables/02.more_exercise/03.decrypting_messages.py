key = int(input())
n = int(input())
message = ''
for x in range(n): message+=chr(ord(input())+key)
print(message)