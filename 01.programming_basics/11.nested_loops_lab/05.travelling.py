destination = input()

while destination!='End':
    money_needed = float(input())
    money_available = 0
    while money_available<money_needed: money_available += float(input())
    print(f'Going to {destination}!')
    destination = input()