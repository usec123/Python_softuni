hour = int(input())
day = input()

if day!='Sunday' and hour in range(10,19): print('open')
else: print('closed')