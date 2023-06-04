def loading_bar(percentage:int)->str:
    if percentage == 100:
        output = f'100% Complete!\n[{"%"*10}]'
    else:
        output = f'{percentage}% [{"%"*(percentage//10)}{"."*(10-(percentage//10))}]\nStill loading...'
    return output
print(loading_bar(int(input())))