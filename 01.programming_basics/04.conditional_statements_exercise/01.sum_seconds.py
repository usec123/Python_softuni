time1 = int(input())
time2 = int(input())
time3 = int(input())

minutes = time1 + time2 + time3
hours = 0

hours = minutes // 60
minutes %= 60

if minutes < 10: minutes = '0'+ str(minutes)

print(f'{hours}:{minutes}')