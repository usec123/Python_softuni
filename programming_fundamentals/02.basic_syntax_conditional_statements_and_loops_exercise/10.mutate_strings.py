string1 = input() # transform into 2
string2 = input()
output = []
for x in range(len(string1)):
    temp = string2[:x+1] + string1[x+1:]
    if temp!=string1 and temp not in output:
        print(temp)
        output.append(temp)