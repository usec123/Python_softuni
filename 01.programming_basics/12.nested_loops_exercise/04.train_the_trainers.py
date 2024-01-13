n = int(input())

cmd = input()

total_grades = 0
total_votes = 0

while cmd!='Finish':
    sum_grades = 0
    for x in range(n):
        grade = float(input())
        sum_grades+=grade
        total_grades+=grade
        total_votes+=1
    print(f'{cmd} - {sum_grades/n:.2f}.')
    cmd = input()
print(f'Student\'s final assessment is {total_grades/total_votes:.2f}.')