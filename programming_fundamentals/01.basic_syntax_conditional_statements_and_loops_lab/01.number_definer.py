i = float(input())
output = ''
if i == 0: output = 'zero'
else:
    if abs(i) < 1: output+='small '
    elif abs(i)>1_000_000: output += 'large '
    output+= 'positive' if i > 0 else 'negative'
print(output)