COLUMNS = 7
ROWS = 6
PLAYERS = 2

class FullColumnError(Exception):
    pass

game_matrix = [
    [0 for _ in range(COLUMNS)]
    for _ in range(ROWS)
    ]

direction_mapper = [
    # row, col
    (-1,0), #up
    (0,-1), #left
    (-1,-1), #up left
    (-1,1), #up right
]

def print_matrix(matrix):
    for row in matrix:
        print(row)
        
def player_move(column,player,matrix):
    for row in range(ROWS-1,-1,-1):
        if matrix[row][column] == 0:
            matrix[row][column] = player
            break
    else:
        raise FullColumnError

    return row,column

def win_check(current_row, current_col,matrix):
    for row_movement, col_movement in direction_mapper:
        count = check_direction(current_row,current_col,row_movement,col_movement,player,matrix)
        
        if count >= 4:
            return True
    return False

def check_direction(current_row,current_col,row_movement,col_movement,player,matrix):
    count = 0
    for i in range(-3,4):
        row_index = current_row+row_movement*i
        col_index = current_col+col_movement*i
        
        if not valid_coords(row_index,col_index):
            continue
        
        if matrix[row_index][col_index] != player:
            continue
        
        count += 1
    return count

def valid_coords(row,col):
    return 0<=row<ROWS and 0<=col<COLUMNS

player = 1
while True:
    try:
        selection = int(input(f'Player {player}, please choose a column: ')) - 1
        if not 0<=selection<COLUMNS:
            raise ValueError
        current_row, current_column = player_move(selection,player,game_matrix)
        print_matrix(game_matrix)
        if win_check(current_row, current_column,game_matrix):
            print(f'Player {player} wins!')
            break
    except ValueError:
        print(f'Player {player}, Please select a number between 1 and {COLUMNS}')
        continue
    except FullColumnError:
        print(f'Player {player}, column {selection+1} is full, please choose another one.')
        continue
        
    
    player = player+1 if player<PLAYERS else 1
