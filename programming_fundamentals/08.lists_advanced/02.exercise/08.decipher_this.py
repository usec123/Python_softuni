msg = input().split()
decrypted_msg=[]
for x in msg:
	num =''
	for char in x:
		if char in '0123456789':
			num+=char
		else:break
	x=x.replace(num,'')
	tempmsg = chr(int(num)) + x
	if len(x)>1:tempmsg = tempmsg[0] + tempmsg[-1] +tempmsg[2:-1:]+tempmsg[1]
	decrypted_msg.append(tempmsg)
print(' '.join(decrypted_msg))