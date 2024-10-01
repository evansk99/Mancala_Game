def initialize_board():
    tiles=int(input("Choose number of tiles per player (range 4-10):"))
    while(tiles<4 or tiles>10):
        tiles=int(input("Please choose a valid number of tiles per player (4-10):"))
    pieces=int(input("Choose number of pieces per tile (range 2-6):"))
    while(pieces<2 or pieces>6):
        pieces=int(input("Please choose a valid number of pieces per tile (2-6):"))
    board=[[pieces]*(tiles+1),[pieces]*(tiles+1)]

    # Print the final board
    for row in board:
        print(row)
    
    return board



def choose_player():
    player=int(input("Type 1 to be Player 1 on the Top Row or 1 to be Player 2 on Bottom Row:"))
    while(player not in [1,2]):
        player=int(input("Player 1-->Type 1\nPlayer 2-->Type 2\n"))
    return player    



def end_game(board,playing):
    if(sum(board[0][0:-1])==0 or sum(board[1][0:-1])==0):
        playing=False
    return playing



def results(board):
    print("GAME IS OVER")
    if(sum(board[0])>sum(board[1])):
        print("PLAYER 1 IS VICTORIOUS!")
    elif(sum(board[0])<sum(board[1])):
        print("PLAYER 2 IS VICTORIOUS!")
    else:
        print("IT IS A TIE!")
    print("FINAL SCORE: " + str(sum(board[0])) + " - " + str(sum(board[1]))) 
