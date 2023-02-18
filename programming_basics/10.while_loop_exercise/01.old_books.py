looking_for = input()

current_book = input()
cnt = 0

while current_book != looking_for:
    if current_book == 'No More Books':break
    cnt+=1
    current_book = input()

if current_book == looking_for: print(f'You checked {cnt} books and found it.')
else: print(f'The book you search is not here!\nYou checked {cnt} books.')