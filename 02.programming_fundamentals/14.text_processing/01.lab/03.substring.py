short = input()
long = input()
while short in long:
    long=long.replace(short,'')
print(long)