max_bad_grades = int(input())

bad_grades = 0
sum_grades = 0
cnt_grades = 0
last_problem = ""

while True:
    task_name = input()
    if task_name == 'Enough':
        print(f'Average score: {sum_grades/cnt_grades:.2f}')
        print(f'Number of problems: {cnt_grades}')
        print(f'Last problem: {last_problem}')
        break
    last_problem = task_name
    grade = int(input())
    sum_grades+=grade
    cnt_grades+=1
    if grade<=4: bad_grades+=1
    if bad_grades==max_bad_grades:
        print(f'You need a break, {bad_grades} poor grades.')
        break