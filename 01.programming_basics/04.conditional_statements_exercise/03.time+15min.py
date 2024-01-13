hours = int(input())
mins = int(input()) + 15

if mins>=60:
    mins-=60
    hours+=1

if hours>=24: hours-=24

print(f'{hours}:{mins:02d}')