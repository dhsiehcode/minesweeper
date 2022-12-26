import random

'''

sets up a 9 x 9 board

a 9 x 9 board has 10 mines.
TODO: find algorithm to disperse mines

'''

board = [['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', '', '']]

playing_board = [['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],
                 ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z']]

visited = [[False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False]]


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
        return board[i][j] == 'x' or board[i - 1][j] == 'x' or board[i][j - 1] == 'x' or board[i - 1][j - 1]

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


def num_local_mines(row, col):
    total = 0
    for i in range(3):
        for j in range(3):
            if (row - 1 + i > 0 and row - 1 + i < 9) and (col - 1 + j > 0 and col - 1 + j < 8):
                # print(row - 1 + i)
                # print(col - 1 + i)
                if board[row - 1 + i][col - 1 + j] == 'x':
                    total += 1

    return total


def local_has_blank(row, col):
    for i in range(3):
        for j in range(3):
            if playing_board[row - 1 + i][col - 1 + j] == '-':
                return True

    return False


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
            # playing_board[row][col] = 'x'
            mines_planted += 1
            total_mines -= 1
            loc[counter][0] = row
            loc[counter][1] = col
            counter += 1

    return loc


'''
playing_board = [['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z']]

move (3,6): 
playing_board = [['z','z','z','z','z','z','z','z','x'],
                 ['z','x','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','x','z','z','z','x','z'],
                 ['z','x','2','1','1','1','z','z','z'],
                 ['1','1','1',' ',' ','2','x','z','z'],
                 [' ',' ',' ','m',' ','2','x','z','z'],
                 ['1','1','1',' ',' ','1','2','x','z'],
                 [' ','x','1',' ',' ',' ','1','2','x']]
                 
move (7, 5)
playing_board = [['z','z','z','z','z','z','z','z','x'],
                 ['z','x','z','z','z','z','z','z','z'],
                 ['z','z','z','z','z','z','z','z','z'],
                 ['z','z','z','x','z','z','z','x','z'],
                 ['z','x','2','1','1','1','2','2','1'],
                 ['1','1','1',' ',' ','2','x','2',' '],
                 [' ',' ',' ','m',' ','2','x','3','1'],
                 ['1','1','1',' ',' ','1','2','x','2'],
                 ['z','x','1',' ',' ',' ','1','2','x']]
'''


def move(i, j):
    if board[i][j] == 'x':
        return False

    # perform DFS in all directions and stops when a block has 0 adjacent
    DFS(i, j)

    display_playing_board()

    # will go through one more time to calculate number for corners
    for row in range(6):
        for col in range(6):
            if local_has_blank(row + 1, col + 1) and local_has_mine(row + 1, col + 1) and playing_board[row + 1][
                col + 1] == 'z':
                if board[row + 1][col + 1] == 'x':
                    fill_adjacent_of_mine(row + 1, col + 1)
                else:
                    playing_board[row][col] = "{}".format(num_local_mines(row + 1, col + 1))

    return True


def fill_adjacent_of_mine(row, col):
    for i in range(3):
        for j in range(3):
            if (row - 1 + i > 0 and row - 1 + i < 9) and (col - 1 + j > 0 and col - 1 + j < 8):
                if playing_board[row - 1 + i][col - 1 + j] == '-':
                    playing_board[row][col] = num_local_mines(row, col)


def DFS(i, j):
    if i < 0 or i > 8:
        return

    if j < 0 or j > 8:
        return

    if visited[i][j]:
        return

    visited[i][j] = True

    if playing_board[i][j] == 'x':
        return

    num = num_local_mines(i, j)

    if playing_board[i][j] == 'z' and num == 0:
        DFS(i - 1, j)
        DFS(i, j - 1)
        DFS(i + 1, j)
        DFS(i, j + 1)
        playing_board[i][j] = '-'
    else:
        playing_board[i][j] = "{}".format(num)
        return


# displays the board
def display_playing_board():
    for i in range(9):
        for j in range(9):
            print(playing_board[i][j] + ",", end=" ")
        print('\n')


# displays the board
def display_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j] + ",", end=" ")
        print('\n')
