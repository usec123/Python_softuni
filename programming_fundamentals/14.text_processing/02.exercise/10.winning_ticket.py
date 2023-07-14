def ticket_validation(ticket):
    if len(ticket) == 20:
        first_half,second_half = ticket[:10:],ticket[10::]
        first_half_checked,second_half_checked = half_checker(first_half), half_checker(second_half)
        if first_half_checked!=False and second_half_checked!=False and first_half_checked==second_half_checked:
            if len(set(first_half+second_half)) == 1:
                return f'ticket "{ticket}" - 10{first_half[0]} Jackpot!'
            else:
                return f'ticket "{ticket}" - \
{min([f"{first_half}".count(first_half_checked) if first_half_checked!=False else 101,f"{second_half}".count(second_half_checked) if second_half_checked!=False else 101])}{first_half_checked if first_half_checked!=False else second_half_checked}'
        return f'ticket "{ticket}" - no match'
    return 'invalid ticket'

def half_checker(half):
    symbol = ''
    count = 0
    for x in half:
        if x in '@#$^':
            if x == symbol:
                count+=1
                if count == 6:
                    return x
            else:
                symbol = x
                count = 1
    return False


tickets = [x.strip() for x in input().split(',')]
for ticket in tickets: print(ticket_validation(ticket))