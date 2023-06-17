employee_rate = sum([int(input()) for _ in range(3)])
students = int(input())

hours = 0
while students>0:
    hours+=1
    if hours%4==0: continue
    students-=employee_rate

print(f'Time needed: {hours}h.')