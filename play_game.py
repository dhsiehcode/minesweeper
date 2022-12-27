import game_manager

game_manager.set_up() # sets up board

print('Here is the board: ')
game_manager.display_playing_board()

print(' Here are the mines: ')
game_manager.display_board()

i = input('Please enter row (i value) of desired target: ')
j = input('Please enter column (j value) of desired target: ')

i = int(i)
j = int(j)

# when first input is illegal
while not game_manager.legal_input(i, j):
    print('Please enter correct input')
    i = input('Please enter row (i value) of desired target: ')
    j = input('Please enter column (j value) of desired target: ')

    i = int(i)
    j = int(j)


game_manager.first_move(i, j)

game_manager.display_playing_board()

while True:

    i = input('Please enter row (i value) of desired target: ')
    j = input('Please enter column (j value) of desired target: ')

    i = int(i)
    j = int(j)

    # when input is illegal
    while not game_manager.legal_input(i, j):
        print('Please enter correct input')
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



