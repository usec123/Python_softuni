class MustContainAtSymbolError(Exception):  # Raise error when the name in the email is less than MIN_LENGTH value.
    pass


class NameTooShortError(Exception):   # Raise error when there is no "@" in the email.
    pass


class InvalidDomainError(Exception):  # Raise error when the domain is not in DOMAINS.
    pass


MIN_LENGTH = 5
DOMAINS = "com", "bg", "net", "org"

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.split(".")[-1] not in DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
