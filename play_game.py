import game_manager

game_manager.set_up() # sets up board

print('Here is the board: ')
game_manager.display_playing_board()

game_manager.f

while True:

    i = input('Please enter row (i value) of desired target: ')
    j = input('Please enter column (j value) of desired target: ')

    i = int(i)
    j = int(j)

    if game_manager.move(i, j):
        game_manager.display_playing_board()
    else:
        print('you lost. here are the mines: \n')
        game_manager.display_board()
        break



