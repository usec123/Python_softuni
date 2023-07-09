points = {}
submissions = {}
banned_users = []

cmd = input()

while cmd!='exam finished':
    cmd = cmd.split('-')
    
    if len(cmd) == 2:
        if cmd[0] not in banned_users:
            banned_users.append(cmd[0])
    
    else:
        user = cmd[0]
        lang = cmd[1]
        pts = int(cmd[2])
        
        key = f'{user}-{lang}'
        
        if key in points.keys() and user not in banned_users:
            if pts > points[key]:
                points[key] = pts
        else:
            points[key] = pts
        
        if lang in submissions.keys():
            submissions[lang]+=1
        else:
            submissions[lang]=1
        
    cmd = input()

print('Results:')
for key,value in points.items():
    key = key.split("-")[0]
    if key not in banned_users:
        print(f'{key} | {value}') 

print('Submissions:')
for key,value in submissions.items():
    print(f'{key} - {value}')