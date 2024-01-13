happiness = list(map(int,input().split()))
factor = int(input())
happiness = [h*factor for h in happiness]
avg = sum(happiness)/len(happiness)
happy = len([i for i in happiness if i >= avg])
if happy >= len(happiness)/2:
	print(f'Score: {happy}/{len(happiness)}. Employees are happy!')
else:
	print(f'Score: {happy}/{len(happiness)}. Employees are not happy!')