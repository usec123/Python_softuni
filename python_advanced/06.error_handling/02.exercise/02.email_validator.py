import re

# Custom Exceptions
class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

# Defining regex pattern
# - we don't need to exclusively check for the @ symbol, as an email wouldn't match without it
pattern = r'(\w+)@\w+(\.\w+)'

while True:
    email = input()
    matches = re.search(pattern,email)
    
    # if an email didn't match it's because it doesn't contain @
    if not matches:
        raise MustContainAtSymbolError('Email must contain @')
    
    # checking the length of the username
    if len(matches.group(1)) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    
    # checking if domain is valid
    if matches.group(2) not in ['.com','.bg','.org','.net']:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    
    # if an exception is to be raised, this code would not be reached
    print('Email is valid')