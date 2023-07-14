def length_valid(username):
    return 2<len(username)<17

def chars_valid(username):
    for char in username:
        if not (char.isalnum() or char in '-_'):
            return False
    return True

def redundancy_valid(username):
    return not ' ' in username

usernames = input().split(', ')
for username in usernames:
    if length_valid(username) and\
        chars_valid(username) and\
        redundancy_valid(username):
            print(username)