name = input()
cnt = 1
grace = True
total = 0

while True:
    grade = float(input())
    if grade<4:
        if grace: grace = False
        else:
            print(f'{name} has been excluded at {cnt} grade')
            break
    else:
        total += grade
        if cnt == 12:
            print(f'{name} graduated. Average grade: {total/12:.2f}')
            break
        cnt+=1