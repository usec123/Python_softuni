money_needed = float(input())
money_available = float(input())

days = 0
days_spending = 0

while True:
    days+=1
    action = input()
    amount = float(input())
    if action == 'spend':
        money_available-=amount
        days_spending+=1
        if money_available < 0: money_available = 0
    else: 
        money_available+=amount
        days_spending = 0
    if days_spending == 5:
        print(f"You can't save the money.\n{days}")
        break
    if money_available >= money_needed:
        print(f'You saved the money for {days} days.')
        break