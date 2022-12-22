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
    if i == 0:
        if j == 0:
            return board[i][j] == 'x' or 
    elif i == 8:


    if j == 0:

    elif j == 8:


def set_up():



    mines_planted = 0
    total_mines = 10
    a = random.randint(1, 10) #inclusive [1, 10]

    while total_mines != 0:
        for
