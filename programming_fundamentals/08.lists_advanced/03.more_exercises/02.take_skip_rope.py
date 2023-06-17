text = input()

digits = []
take_list = []
skip_list = []
non_numbers = []

for char in text:
    if char in [str(x) for x in range(10)]:
        digits.append(int(char))
    else:
        non_numbers.append(char)

for x in range(len(digits)):
    if x%2==0:
        take_list.append(digits[x])
    else:
        skip_list.append(digits[x])

taken = ''

for x in range(len(digits)//2):
    to_take = take_list.pop(0)
    to_skip = skip_list.pop(0)
    for x in range(to_take):
        if len(non_numbers) == 0: break
        taken += non_numbers.pop(0)
    non_numbers = non_numbers[to_skip::]

print(taken)