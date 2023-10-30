class InvalidSelectionError(Exception):
    pass
class SelectionNotInRangeError(Exception):
    pass

direction_mapper = [
    (1,0), #u/d
    (0,1), #l/r
    (1,1), #ur/dl
    (1,-1) #dr/ul
]

def setup():
    COLS = 3
    ROWS = 3
    P1 = input('Player one name: ')
    P2 = input('Player two name: ')
    P1_SIGN = input(f'{P1}, would you like to play with \'X\' or \'O\'? ')
    while P1_SIGN not in 'XO':
        P1_SIGN = input(f'Invalid sign, please choose \'X\' or \'O\': ')
    P2_SIGN = ''.join('XO'.split(P1_SIGN))

    PL1 = [P1,P1_SIGN]
    PL2 = [P2,P2_SIGN]
    
    matrix = [
        [' ' for _ in range(COLS)]
        for _ in range(ROWS)
    ]

    print('This is the numeration of the board:\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |')
    print(f'{PL1[0]} starts first!')
    return (PL1,PL2,matrix)

def print_matrix(matrix):
    for row in matrix:
        print('| ',end='')
        print(' | '.join(row),end='')
        print(' |')

def make_move(player_sign, selection, matrix):
    selection = (selection//3,selection%3)
    
    if matrix[selection[0]][selection[1]] == ' ':
        matrix[selection[0]][selection[1]] = player_sign
        return check_win(matrix,player_sign,selection) # True - win, None - no win
    raise InvalidSelectionError

def check_win(matrix,player,selection):
    for row_movement, col_movement in direction_mapper:
        count = 0
        for x in range(-2,3):
            row_index = selection[0]+row_movement*x
            col_index = selection[1]+col_movement*x
            if validate_coords((row_index,col_index),matrix):
                if matrix[row_index][col_index] == player:
                    count+=1
                else:
                    continue
            else:
                continue
        if count>=3:
            return True
    return None

def check_draw(matrix):
    for x in matrix:
        if ' ' in x:
            return False
    return True

def validate_coords(coords,matrix):
    return coords[0] in range(len(matrix)) and coords[1] in range(len(matrix[0]))

PLAYER1, PLAYER2, game_matrix = setup()

while True:
    try:
        selection = int(input(f'{PLAYER1[0]}, choose a free position [1-9]: '))-1
        if selection in range(9):
            result = make_move(PLAYER1[1],selection,game_matrix)
            if result == None:
                print_matrix(game_matrix)
                if check_draw(game_matrix):
                    print('Draw!')
                    break
                PLAYER1,PLAYER2=PLAYER2,PLAYER1
                continue
            else:
                print(f'Player {PLAYER1[0]} wins!')
                print_matrix(game_matrix)
                break
        raise SelectionNotInRangeError
    except InvalidSelectionError:
        print('Invalid selection, please try again!')
    except ValueError:
        print('Selection must be an integer!')
    except SelectionNotInRangeError:
        print('Selection must be in the range [1-9]!')