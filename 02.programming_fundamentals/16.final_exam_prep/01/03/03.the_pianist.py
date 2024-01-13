n = int(input())

composers = {}
keys = {}

for _ in range(n):
    cmd = input().split('|')
    piece = cmd[0]
    composer = cmd[1]
    key = cmd[2]
    
    composers[piece] = composer
    keys[piece] = key

cmd = input()
while cmd!='Stop':
    cmd = cmd.split('|')
    
    if cmd[0] == 'Add':
        piece = cmd[1]
        composer = cmd[2]
        key = cmd[3]
        if piece in composers:
            print(f'{piece} is already in the collection!')
        else:
            composers[piece] = composer
            keys[piece] = key
            print(f'{piece} by {composer} in {key} added to the collection!')
    
    elif cmd[0] == 'Remove':
        piece = cmd[1]
        if piece in composers:
            composers.pop(piece)
            keys.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    
    elif cmd[0] == 'ChangeKey':
        piece = cmd[1]
        new_key = cmd[2]
        if piece in keys:
            keys[piece] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    
    cmd = input()

for piece in composers.keys():
    print(f'{piece} -> Composer: {composers[piece]}, Key: {keys[piece]}')