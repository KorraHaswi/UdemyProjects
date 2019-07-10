
import random



#DISPLAYS AND EMPTY BOARD
def display_board(b):
    print("  " +  b[7]+ "| " + b[8] +" |" + b[9] +"  ")
    print("-----------")
    print("  " + b[4]+ "| "  + b[5] +" |" + b[6] +"  ")
    print("-----------")
    print("  " + b[1]+ "| "  + b[2] +" |" + b[3] +"  ")

#PLAYER INPUT. IT CAN BE AN X OR 0. THIS FUNCTION RETURNS A TUPLE. ONE FOR THE FOR THE PLAYER1 AND OTHER FOR PLAYER2
def playerInput():
    pI=' '
    while not(pI == 'X' or pI == 'O'):
    # this is same as while pI != 'X' and pI != 'O'
        pI=input('player1 do you want to be X or O?').upper()
    if pI == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
#NOW THAT WE HAVE THE INPUT FROM THE PLAYER. WE SHOULD BE ABLE TO PLACE IT IN THE BOARD THIS FUNCTION PLACES THE PLAYER INPUT IN THE FUCNTION
def placePlayerInput(board, pI, position):
    board[position] = pI




# THIS FUNCTION CHECKS  IF THE GAME IS WON OR NOTplacePlayerInput(theBoard,'X',7)
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

#A FUNCTION TATH RANDOMLY DECIDES WHO WILL PLAY FIRST
def choose_first():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'

#A FUNCTION THAT CHECK FOR EMPTY SPACE IN THE BOARD
def space_check(board, position):
    return board[position] == ' '

#FUNCTION THAT CHECK IF THE BOARD IS FULL OR NOT
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# FUNCTION THAT ASKS PLAYERS NEXT POSITION AND ALS USE SPACE_CHECK() TO SEE IF THAT POSTION IS AVAILABLE
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("choose your next position: (1-9)"))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# THE MAIN ALGORITHM IS BELOW

print('Welcome to Tic Tac Toe!')
while True:
    #reset the board
    theBoard=[' '] *10
    player1_marker, player2_marker = playerInput()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Are you ready to play the game?, enter Yes or No')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':

            display_board(theBoard)
            position = player_choice(theBoard)
            placePlayerInput(theBoard, player1_marker, position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations you have own the game')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'player2'


        else:
            #Player2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            placePlayerInput(theBoard,player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player2 has  won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break

                else:
                    turn = 'player1'

    if not replay():
                break








