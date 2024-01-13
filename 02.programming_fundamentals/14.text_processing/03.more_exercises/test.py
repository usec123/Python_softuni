print(sum([
    ord(x) 
    for x in '123456789' 
    if x in range(ord('1'),ord('7')+1)]))