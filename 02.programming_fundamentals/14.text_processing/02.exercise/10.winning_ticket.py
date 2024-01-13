def ticket_validation(ticket):
    if len(ticket) == 20:
        first_half,second_half = ticket[:10:],ticket[10::]
        first_half_checked,second_half_checked = half_checker(first_half), half_checker(second_half)
        if first_half_checked!=False and second_half_checked!=False:
            if len(set(first_half+second_half)) == 1:
                return f'ticket "{ticket}" - 10{first_half[0]} Jackpot!'
            else:
                return f'ticket "{ticket}" - {min(first_half_checked[1],second_half_checked[1])}{first_half_checked[0] if first_half_checked[1]>second_half_checked[1] else second_half_checked[0]}'
        return f'ticket "{ticket}" - no match'
    return 'invalid ticket'

def half_checker(half:str):
    symbol = ''
    count = 0
    max_count,max_symbol = 0,''
    for current_symbol in half:
        if current_symbol in '@#$^':
            if current_symbol == symbol:
                count+=1
            else:
                if count > max_count:
                    max_count = count
                    max_symbol = symbol
                symbol = current_symbol
                count = 1
        else:
            if count>max_count:
                max_count = count
                max_symbol = symbol
            symbol = ''
            count = 0
    if count>max_count:
        max_count = count
        max_symbol = symbol
    if max_count > 5:
        return [max_symbol,max_count]
    return False


tickets = [x.strip() for x in input().split(',')]
for ticket in tickets: print(ticket_validation(ticket))