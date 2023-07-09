MINIMUM_AVERAGE_GRADE = 4.5

n = int(input())

grades = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name in grades.keys():
        grades[name].append(grade)
    else:
        grades[name] = [grade]

for student,all_grades in grades.items():
    average_grade = sum(all_grades)/len(all_grades)
    if average_grade >= MINIMUM_AVERAGE_GRADE:
        print(f'{student} -> {average_grade:.2f}')