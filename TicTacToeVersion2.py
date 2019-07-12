import random

#FUNCTIN THAT DISPLAYS THE BOARD

def boardDisplay(b):
    print("  " + b[7] + "| " + b[8] + " |" + b[9] + "  ")
    print("-----------")
    print("  " + b[4] + "| " + b[5] + " |" + b[6] + "  ")
    print("-----------")
    print("  " + b[1] + "| " + b[2] + " |" + b[3] + "  ")


#FUNCTION THAT DETERMINES WHOSE TURN IS FIRST

def turn():
    if random.randint(0,1) == 1:
        return 'player1'
    else:
        return 'player2'

#FUNCTION THAT ASSIGN MARKERS TO THE PLAYERS
def playerInput():
    while True:
        marker = ' '
        marker = input('Enter the input').upper()
        if marker == 'X':
            return ('X', 'O')
            break

        elif marker == 'O':
            return ('O', 'X')
            break

# CHECK SPACE
def CheckIfThereIsAnySpaceOnBoard(board, position):
    return board[position] == ' '

# CHECK IF THE BOARD IS FULL
def CheckIfTheBoardIsFUll(board):
    for i in range(1, 10):
        if CheckIfThereIsAnySpaceOnBoard(board, i):
            return False
    return True



#FUNCTION  THAT TAKES PLAYER POSITION AND MARKER AND PUT IN TH EBOARD
def placePlayerInput(board,marker,position):
    board[position] = marker
#FUCNTION THAT CHECKS PLAYERS MOVE ON THE BOARD
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not CheckIfThereIsAnySpaceOnBoard(board,position):
        position = int(input('enter a number between 1-9'))
    return position


'''def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal'''

def win_check(b, mark):
    case1 = (b[7] == mark and b[5] == mark and b[3] == mark)
    case2 = (b[1] == mark and b[5] == mark and b[9] == mark)
    case3 = (b[7] == mark and b[8] == mark and b[9] == mark)
    case4 = (b[4] == mark and b[5] == mark and b[6] == mark)
    case5 = (b[1] == mark and b[2] == mark and b[3] == mark)
    case6 = (b[7] == mark and b[4] == mark and b[1] == mark)
    case7 = (b[8] == mark and b[5] == mark and b[2] == mark)
    case8 = (b[9] == mark and b[6] == mark and b[3] == mark)
    if case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8:
        return True


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
#GAME LOGIC

print("Welcome to TIc Tac Toe!")

while True:
    theBoard = [' ']*10
    #display the board
    boardDisplay(theBoard)
    player1_marker, player2_marker = playerInput()
    bari = turn()
    print(bari + ' will go first')

    play_game = input('Are you ready to play the game, enter yes or no')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if bari == 'player1':
            boardDisplay(theBoard)
            position = player_choice(theBoard)
            placePlayerInput(theBoard,player1_marker, position)

            if win_check(theBoard,player1_marker):
                boardDisplay(theBoard)
                print("you have won the game")
                game_on = False
            else:
                if CheckIfTheBoardIsFUll(theBoard):
                    boardDisplay(theBoard)
                    print('the game is a tie')
                    break
                else:
                    bari = 'player2'
        else:
            bari == 'player2'
            boardDisplay(theBoard)
            position = player_choice(theBoard)
            placePlayerInput(theBoard, player2_marker, position)

            if win_check(theBoard, player1_marker):
                boardDisplay(theBoard)
                print("you have won the game")
                game_on = False
            else:
                if CheckIfTheBoardIsFUll(theBoard):
                    boardDisplay(theBoard)
                    print('the game is a tie')
                    break
                else:
                    bari = 'player1'

    if not replay():
        break




















