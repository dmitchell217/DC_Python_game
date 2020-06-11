# this function is continually called by the game running function to update the board
def display_board(moves):
# '''
# Inputs: 9 postions on board. Left to right. Top to bottom form(X/O/#)
# Input ex. # moves = ['X', 'O','X', 'O','X', 'O','X', '','X']
# Outputs: Prints a board filled with Xs/Os/_s
# Functionality: working
# '''
    print(f' {moves[0]} | {moves[1]} | {moves[2]} \n__________\n {moves[3]} | {moves[4]} | {moves[5]} \n __________\n {moves[6]} | {moves[7]} | {moves[8]}')