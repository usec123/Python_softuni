cmd = input()
tasks = []
while cmd.split('-')[0]!='End':
    tasks.append(cmd)
    cmd = input()
tasks = sorted(tasks, key=lambda x: int(x.split('-')[0]))
tasks = [element.split('-')[1] for element in tasks]
print(tasks)