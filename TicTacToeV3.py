import os
import time

board=[' ']*10
player = 1
# Win Flags
Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running


# THIS FUNCTION DRAWS THE BOARD
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# THIS FUNCTION CHECKS IF THE BOARD IS EMPTY OR NOT
def checkPosition(position):
    if board[position] == ' ':
        return True
    else:
        return False


# my function is not working properly. need to investigate it. 
'''def win_check(b,mark):
    case1 = (b[7] == mark and b[5] == mark and b[3] == mark)
    case2 = (b[1] == mark and b[5] == mark and b[9] == mark)
    case3 = (b[7] == mark and b[8] == mark and b[9] == mark)
    case4 = (b[4] == mark and b[5] == mark and b[6] == mark)
    case5 = (b[1] == mark and b[2] == mark and b[3] == mark)
    case6 = (b[7] == mark and b[4] == mark and b[1] == mark)
    case7 = (b[8] == mark and b[5] == mark and b[2] == mark)
    case8 = (b[9] == mark and b[6] == mark and b[3] == mark)
    if case1 or case2 or case3 or case4 or case5 or case6 or case7 or case8:
        Game = Win
    elif (b[1] != ' ' and b[2] != ' ' and  b[3] != ' ' and b[4] != ' ' and b[5] != ' ' and b[6] != ' ' and b[7] != ' ' and b[8] != ' '  and b[9] != ' '):
        Game = Draw
    else:
        Game = Running'''
def CheckWin():
    global Game
    #Horizontal winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    #Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=Win
    #Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=Win
    #Match Tie or Draw Condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
    else:
        Game=Running



print("Tic Tac Toe Game")
print("Player 1 [X] --- Player 2 [O]\n")
while Game == Running:
    DrawBoard()
    if ( player % 2 != 0):
        print('player 1 chance')
        Mark = 'X'
    else:
        print('player2 chance')
        Mark = 'O'
    choice = int(input("Enter the position between 1 to 9"))
    if checkPosition(choice):
        board[choice] = Mark
        player = player+1
        CheckWin()
    DrawBoard()
    if  Game == Draw:
        print("Game is Draw")
    elif Game == Win:
        player = player -1
        if (player % 2):
            print("player 1 won")
        else:
            print("player 2 won")
