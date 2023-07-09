cmd = input().split(':')
students = {}
while len(cmd)>1:
    students[cmd[0]+':'+cmd[1]] = cmd[2]
    cmd = input().split(':')
for x in students.keys():
    x = str(x)
    if students[x] == cmd[0].replace('_',' '):
        print(' - '.join(x.split(':')))