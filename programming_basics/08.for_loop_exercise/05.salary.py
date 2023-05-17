n = int(input())
salary = int(input())
lost_salary = False
for x in range(0,n):
    website = input()
    if website == 'Facebook': salary-=150
    if website== 'Instagram': salary-=100
    if website=='Reddit': salary-=50
    if salary<=0: 
        lost_salary = True
        break
if lost_salary: print('You have lost your salary.')
else: print(salary)