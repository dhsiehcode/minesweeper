import game_manager

game_manager.set_up() # sets up board

print('Here is the board: \n')
game_manager.display_playing_board()

while True:

    i = input('Please enter row (i value) of desired target: ')
    print('\n')
    j = input('Please enter column (j value) of desired target: ')
    print('\n')

    if game_manager.move(i, j):
        game_manager.display_playing_board()
    else:
        print('you lost. here are the mines: \n')
        game_manager.display_board()
        break



