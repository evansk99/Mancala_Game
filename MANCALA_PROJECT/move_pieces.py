### Fully fledged and improved in the final version in Play_Game file ###
## Not needed to run the game !!##

def move_pieces(board,player):
    #player=player-1
    tile=int(input("Choose a NON-EMPTY tile from your row:"))
    while(tile>=int((len(board[0])-1)) or tile<0 or board[player][tile]==0):
        print("Invalid move")
        tile=int(input("Tile Number must be from 0 to " + str(len(board[0])-2) + " and it must be a NON-EMPTY tile:"))
    
    # Get the value from the chosen cell
    pieces = board[player][tile]
    TilesPerPlayer=len(board[0])
    times=0

    # Set the chosen cell to 0
    board[player][tile] = 0
    
    # Split the value into 1s
    ones = pieces
    while(ones>0):

        ##  RULE 1  ##
        # Distribute the 1s
        # Start distributing to (2,6) and skip (1,6)
        
        if (times==0):
            for c in range(tile+1, TilesPerPlayer, 1):  # Go from starting tile to (2,6)
                if ones > 0:
                    board[player][c] += 1
                    ones -= 1
                    last_row=player
                    last_col=c
            times=1
        else:
            
            for c in range(0, TilesPerPlayer, 1):  # Go through second player
                if ones > 0:
                    board[player][c] += 1
                    ones -= 1
                    last_row=player
                    last_col=c
            
        other_player_row = 0 if player == 1 else 1
        for c in range(0, TilesPerPlayer):  # Now distribute to the first player, skip (1,6)
            if c == TilesPerPlayer-1:  # Skip (1,6)
                continue
            if ones > 0:
                board[other_player_row][c] += 1
                ones -= 1
                last_row=other_player_row
                last_col=c

        ##  RULE 2  ##
        if(board[last_row][last_col]==1 and last_col!=TilesPerPlayer-1 and player==last_row and board[0][last_col]+board[1][last_col]>1): 
            board[last_row][TilesPerPlayer-1]=board[last_row][TilesPerPlayer-1]+board[0][last_col]+board[1][last_col]
            board[0][last_col]=0
            board[1][last_col]=0

        # Print the final board
        for row in board:
            print(row)
        
    ##  RULE 3  ##

    if (pieces%(2*TilesPerPlayer-1)==TilesPerPlayer-1-tile):
        print("PLAY AGAIN")#############FIX
        return board,player
        
    player=other_player_row                
    return board,player
