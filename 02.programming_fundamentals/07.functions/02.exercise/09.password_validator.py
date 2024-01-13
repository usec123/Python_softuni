def validator(password:str):
    valid = True
    if not 5<len(password)<11:
        print("Password must be between 6 and 10 characters")
        valid = False
    letters = []
    digits = []
    for letter in range(ord('a'),ord('z') + 1):
        letters.append(chr(letter))
    for x in range(10):
        digits.append(str(x))
    for char in password.lower():
        if not (char in letters or char in digits):
            valid=False
            print("Password must consist only of letters and digits")
            break
    digits_count = 0
    for char in password:
        if char in digits:
            digits_count+=1
        if digits_count == 2:
            break
    if digits_count < 2:
        valid = False
        print("Password must have at least 2 digits")
    if valid:
        print('Password is valid')

validator(input())