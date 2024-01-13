def sorting_cheeses(**kwargs):
    output = ''
    kwargs = dict(sorted(kwargs.items(),key=lambda kvp: (-len(kvp[1]),kvp[0])))
    for key,value in kwargs.items():
        kwargs[key] = sorted(value,key=lambda x: -x)
        output+=f'{key}\n'
        output += '\n'.join(str(qty) for qty in kwargs[key])
        output+='\n'
    return output

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
