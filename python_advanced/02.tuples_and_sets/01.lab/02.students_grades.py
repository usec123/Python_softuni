n = int(input())

students = {}

for _ in range(n):
    student, grade = input().split()
    if student in students:
        students[student].append(float(grade))
    else:
        students[student] = [float(grade)]
    
for student, grades in students.items():
    print(f'{student} -> {" ".join([f"{grade:.2f}" for grade in grades])} (avg: {sum([g for g in grades])/len(grades):.2f})')