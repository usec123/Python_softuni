import re

def regex_test(regex,string):
    match = re.search(regex, string)
    if match: print('match found:',match.group())
    else: print('no match found')

regex_test('\\bworld\\b', 'hello world') # boundary
regex_test('\\d', '12455') # digit
regex_test('\\d+', '12455') # more digits
regex_test('\\s', 'something important') # white spaces
regex_test('\\S+', 'something important') # no white spaces
regex_test('\\w+', 'something_important123 asdd') # word
regex_test('\\W+', 'something_important123 ?>< asdd') # no word
regex_test('\\W+', 'something_important123 ?>< asdd') # no word


regex_test('\d+\.\d+','The cost is 12.99 lv.') # more than one digit, then dot, then more than one digit
print(re.findall('\d+\.\d+','The cost is 12.99 lv.')) # finds all -> list
print(re.findall('hi*', 'h hi hii hiii hiiii')) # *
print(re.findall('dog|cat','i have a dog and a cat')) # |
print(re.findall('(red|blue) and (big|small)','The ball is blue and big')) # |
print(re.findall('\\d{3}', '123 112233 1452 81 8541 255 311')) # {3} - 3 digits
print(re.findall('^Python', 'Python is fun')) # Begins with
print(re.findall('Python$', 'Language - Python')) # Begins with
print(re.findall('(?P<shortwords>\w)(?P<shortdigits>\d)(?P<longwords>[a-zA-Z]+)(?P<longdigits>\d+)','w4word420'))