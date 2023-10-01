from collections import deque

text = deque(input().split())

PRIMARY = ['red','yellow','blue']
SECONDARY = {
    'orange': ['red','yellow'],
    'purple': ['red','blue'],
    'green': ['yellow','blue']
}

found_colors = []
secondary_colors = set()

while text:
    str1=text.popleft()
    if text:
        str2=text.pop()
        to_check_list = [str1+str2,str2+str1]
    else:
        to_check_list = [str1]
        
    to_insert = True
    for to_check in to_check_list:
        for x in PRIMARY+list(SECONDARY.keys()):
            if x == to_check:
                if x in PRIMARY or x in SECONDARY:
                    found_colors.append(to_check)
                if x in SECONDARY:
                    secondary_colors.add(to_check)
                to_insert = False
                break
    
    if to_insert:
        str1 = str1[:-1:]
        str2 = str2[:-1:]
        
        if str2:
            text.insert(len(text)//2,str2)
        if str1:
            text.insert(len(text)//2,str1)

for x in secondary_colors:
    for req in SECONDARY[x]:
        if req not in found_colors:
            while x in found_colors:
                found_colors.remove(x)

found_colors = [color for color in found_colors if color in PRIMARY or color in secondary_colors]

print(found_colors)