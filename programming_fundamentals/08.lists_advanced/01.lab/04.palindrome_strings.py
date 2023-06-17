string = input().split()
palindrome = input()

print([word for word in string if word == word[::-1]])
print(f'Found palindrome {string.count(palindrome)} times')