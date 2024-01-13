l = int(input())/10
w = int(input())/10
h = int(input())/10
percent_taken = float(input())

volume = l*w*h
volume *= 1 - (percent_taken/100)

print(volume)