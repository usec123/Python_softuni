name = input()

total_students = 0
total_standards = 0
total_kids = 0

while name!='Finish':
    free_places = int(input())
    student_places = 0
    standard_places = 0
    kid_places = 0
    for x in range(free_places):
        ticket_type = input()
        if ticket_type == 'End': break
        elif ticket_type == 'student': student_places+=1
        elif ticket_type == 'standard': standard_places+=1
        else: kid_places+=1
    total_students += student_places
    total_standards += standard_places
    total_kids += kid_places
    print(f'{name} - {((student_places+standard_places+kid_places)/free_places) * 100:.2f}% full.')
    name = input()
total_tickets = total_students+total_standards+total_kids
print(f'Total tickets: {total_tickets}')
print(f'{total_students*100/total_tickets:.2f}% student tickets.')
print(f'{total_standards*100/total_tickets:.2f}% standard tickets.')
print(f'{total_kids*100/total_tickets:.2f}% kids tickets.')