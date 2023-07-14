cmd = input().split(':')
students = []
while len(cmd)>1:
    students.append({'name':cmd[0], 'ID':cmd[1], 'course':cmd[2]})
    cmd = input().split(':')
for x in students:
    if x['course']==cmd[0].replace('_',' '):
        print(f'{x["name"]} - {x["ID"]}')