version = list(map(int, input().split('.')))[::-1]
version[0]+=1
for i in range(len(version)):
	if version[i]==10:
		version[i] = 0
		version[i+1] += 1
print('.'.join(str(i) for i in version[::-1]))