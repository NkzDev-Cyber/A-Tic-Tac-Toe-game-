# TicTacToe-Python v1.0
# Created by: NkzDev-Cyber


board = [" " for i in range(9)]


def show_board():
    print ("\n")
    print (board [0] + " | " + board [1] + " | " + board [2] + " | ")
    print ("--+---+--+")
    print (board [3] + " | " + board [4] + " | " + board [5] + " | ")
    print ("--+---+--+")
    print (board [6] + " | " + board [7] + " | " + board [8] + " | ")
    
def check_win():
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != " ":
            return True
        
    return False
    
player = "x"


while True:
    show_board()
    choice = int (input (f"\n player {player}, choose a position (1-9: "))
    
    
    if board[choice - 1] == " ":
        board[choice - 1] = player
        
    else:
        print ("Position Already Taken!!!")
        continue
    
    if check_win():
        show_board()
        print (f"\n player {player} won!!! yay :3")
        break
    
    if player == "x":
        player = "o"
        
    else:
        player = "x"
