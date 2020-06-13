# this function runs the game. it will set up the game and walk the user through it
import random
import display_board
from winner import winner
def run_game():
    # Player one is Xs
    # Player two is Os
    # initialize moves array
    moves = []
    [moves.append('') for x in range(0,9)]
    count = 0
    player_flip = True
    while count < 40: # eventually, run until a return condition is met
        if player_flip:
            index = int(input('Player 1, what is your move? '))
            if index not in range(0,9):
                print('Input must be a digit between 0-8')
                continue
            if (moves[index] == ''):
                moves[index] = 'X'
            else: 
                print('A move has already been played here.')
                continue
        else:
            index = random.randint(0,8)
            print("\n")
            if index not in range(0,9):
                continue
            if (moves[index] == ''):
                moves[index] = 'O'
            else: 
                continue
    # check to see if game is over
        if winner(moves, 'X'):
            display_board.display_board(moves)
            print('Congrats Player 1! You win!')
            return True
        elif winner(moves, 'O'):
            display_board.display_board(moves)
            print('You lost: the bullies are going to take your lunch for the next year. Get better at Tic Tac Toe. Start over to cultivate another garden')
            return False
        if '' not in moves:
            display_board.display_board(moves)
            print('The game finished with no winner... Try harder next time.')
            return True
        player_flip = not player_flip
        count+=1 # to prevent infinite loop while testing
        display_board.display_board(moves)
    return