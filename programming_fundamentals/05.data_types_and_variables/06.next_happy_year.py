current_year = int(input())
year_to_check = current_year+1
while True:
    unique = True
    checking_year = list(str(year_to_check))
    while len(checking_year)>0:
        char = checking_year.pop()
        if char in checking_year:
            unique = False
            break
    if unique:
        print(year_to_check)
        break
    year_to_check+=1
    

#set(list) => returns a  sorted list with unique elements only