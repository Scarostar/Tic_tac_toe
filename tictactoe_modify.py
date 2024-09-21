import numpy as np
import random
from time import sleep

def empty_board():
    board = np.array([
                                    ['-','-','-'],
                                    ['-','-','-'],
                                    ['-','-','-']
                                ])
    return board

def empty_places(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] =='-':
                l.append((i,j))
    return l

def random_place(board, player):
    select = empty_places(board)
    current_location = random.choice(select)
    board[current_location] = player
    return(board)

def user_place(board, player):
    while True:
        print(player, "'s turn")
        move = input("Enter row and column where u want to place your mark as (row/column)")
        mlist = move.split("/")
        print(mlist)
        row = int(mlist[0])
        col = int(mlist[1])
        if (row-1,col-1) in empty_places(board):
            board[row-1][col-1] = player
            break
        elif row <=3 and col <= 3:
            print("Space already occupied, try again")
            continue
        else:
            print("Out of range, try again")
            continue
    return board
def row_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                continue

        if win == True:
            return(win)
    return(win)

def column_winner(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return(win)
    return(win)

def diag_winner(board, player):
    win = True
    for x in range(len(board)):
        if board[x][x] != player:
            win = False

    if win == True:
        return(win)
    
    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x][y] != player:
            win = False
            
    return(win)

def eval_winner(board):
    winner = '-'
    for player in ['X','O']:
        if row_winner(board, player) or column_winner(board, player) or diag_winner(board, player):
            winner = player
    if np.all(board != '-') and winner == '-':
        winner = -1
    return winner

def CPU_start():
    board = empty_board()
    winner = '-'
    counter = 1
    print(board)
    sleep(2)

    user_player = input("Choose your mark (X/O)").upper()
    while user_player not in ["X", "O"]:
            print("Invalid choice, try again")
    if user_player == "X":
        ai_player = "O"
    elif user_player == "O":
        ai_player = "X"
    
    while winner == '-':
        if user_player == "X":
            for player in [user_player, ai_player]:
                if player == user_player:
                    board = user_place(board, player)
                elif player == ai_player:
                    board = random_place(board,player)
                print("Board after", str(counter), "moves")
                print(board)
                sleep(2)
                counter +=1
                winner = eval_winner(board)

                if winner != '-':
                    break
        else:
            for player in [ai_player, user_player]:
                if player == user_player:
                    board = user_place(board, player)
                elif player == ai_player:
                    board = random_place(board,player)
                print("Board after", str(counter), "moves")
                print(board)
                sleep(2)
                counter +=1
                winner = eval_winner(board)

                if winner != '-':
                    break            
    return(winner)

def PVP_start():
    board = empty_board()
    winner = '-'
    counter = 1
    print(board)
    sleep(2)

    user_player1 = "X"
    user_player2 = "O"
    while winner == '-':
        for player in [user_player1, user_player2]:
            if player == user_player1:
                board = user_place(board, user_player1)
            elif player == user_player2:
                board = user_place(board, user_player2)
            print("Board after", str(counter), "moves")
            print(board)
            sleep(2)
            counter +=1
            winner = eval_winner(board)

            if winner != '-':
                break
    return(winner)

ch = int(input("Enter 1 to play vs CPU, 2 to play vs player"))
if ch == 1:
    game_winner = CPU_start()
    if game_winner=="X":
        print("Winner of the game is player 1 (X)")
    elif game_winner=="O":
        print("Winner of the game is player 2 (O)")
    else:
        print("The game is a tie")
if ch == 2:
    game_winner = PVP_start()
    if game_winner=="X":
        print("Winner of the game is player 1 (X)")
    elif game_winner=="O":
        print("Winner of the game is player 2 (O)")
    else:
        print("The game is a tie")
