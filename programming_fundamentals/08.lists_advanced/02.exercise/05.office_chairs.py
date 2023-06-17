n=int(input())
left = 0
to_print = True

for i in range(n):
	cmd = input().split()
	chairs = len(cmd[0])
	visitors = int(cmd[1])
	if chairs >= visitors:
		left += chairs - visitors
	else:
		print(f'{visitors - chairs} more chairs needed in room {i+1}')
		to_print = False
if to_print: print(f'Game On, {left} free chairs left')