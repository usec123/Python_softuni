cmd = input()

courses = {}

while cmd!='end':
    cmd = cmd.split(' : ')
    course_name = cmd[0]
    student_name = cmd[1]
    
    if course_name in courses.keys():
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]
    
    cmd = input()
    
for course in courses:
    print(f'{course}: {len(courses[course])}')
    for student in courses[course]:
        print(f'-- {student}')