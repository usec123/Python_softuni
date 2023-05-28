budget = int(input())
cmd = input()
while cmd!='End':
    budget-=int(cmd)
    if budget < 0: break
    cmd = input()
if cmd == 'End': print('You bought everything needed.')
else: print('You went in overdraft!')