import random


'''

sets up a 9 x 9 board

a 9 x 9 board has 10 mines.
TODO: find algorithm to disperse mines

'''


board = [['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','',''],
         ['','','','','','','','','']]

# returns if there are mines locally around i, j
def local_has_mine(i, j):
    # the four corners

    if i == 0 and j == 0:
        return board[i][j] == 'x' or board[i + 1][j] == 'x' or board[i][j + 1] == 'x' or board[i + 1][j + 1]
    elif i == 0 and j == 8:
        return board[i][j] == 'x' or board[i][j - 1] == 'x' or board[i + 1][j] == 'x' or board[i + 1][j - 1]
    elif i == 8 and j == 0:
        return board[i][j] == 'x' or board[i][j + 1] == 'x' or board[i - 1][j] == 'x' or board[i - 1][j + 1]
    elif i == 8 and j == 8:
        return  board[i][j] == 'x' or board[i - 1][j] == 'x' or board[i][j - 1] == 'x' or board[i - 1][j - 1]

    # on the walls
    if i == 0:
        return board[i][j - 1] == 'x' or board[i][j] == 'x' or board[i][j + 1] or board[i + 1][j - 1] == 'x' or \
               board[i + 1][j] == 'x' or board[i + 1][j + 1]
    elif i == 8:
        return board[i][j - 1] == 'x' or board[i][j] == 'x' or board[i][j + 1] or board[i - 1][j - 1] == 'x' or \
               board[i - 1][j] == 'x' or board[i - 1][j + 1]

    elif j == 0:
        return board[i - 1][j] == 'x' or board[i][j] == 'x' or board[i + 1][j] or board[i - 1][j + 1] == 'x' or \
               board[i][j + 1] == 'x' or board[i + 1][j + 1]
    elif j == 8:
        return board[i - 1][j] == 'x' or board[i][j] == 'x' or board[i + 1][j] or board[i + 1][j - 1] == 'x' or \
               board[i][j - 1] == 'x' or board[i + 1][j - 1]

    # all 8 corners
    return board[i][j] == 'x' or board[i - 1][j - 1] == 'x' or board[i][j - 1] == 'x' or board[i + 1][j - 1] or \
           board[i - 1][j] == 'x' or board[i + 1][j] or board[i - 1][j + 1] or board[i][j + 1] or board[i + 1][j + 1]


# sets up the board with mines

def set_up():


    counter = 0
    mines_planted = 0
    total_mines = 10
    # 2 D list with all locations of the bombs
    loc = [[0] * 2] * 10

    while total_mines != 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        a = random.randint(1, 10)
        if local_has_mine(row, col):
            bound = 6
        else:
            bound = 3

        # add mine
        if a > bound:
            board[row][col] = 'x'
            mines_planted += 1
            total_mines -= 1
            loc[counter][0] = row
            loc[counter][1] = col
            counter += 1

    return loc



