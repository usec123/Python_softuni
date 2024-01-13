def grocery_store(**kwargs):
    groceries = {}
    for key,value in kwargs.items():
        groceries[key] = value
    groceries = sorted(groceries.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
    return '\n'.join([f'{new_key}: {new_value}' for new_key, new_value in groceries])

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
