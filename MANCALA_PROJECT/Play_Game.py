import copy

#This function considers the set of rules that are present in the Mancala Game and moves the piece on the board in a valid manner
#board:2xN matrix that contains N-1 playable tiles for each player while the N-th tile saves the score of each player at any point of the game
#player:integer 0 or 1 that determines if it is the turn of player 1 in the top row of the matrix or player 2 in the bottom row ro play
#tile:integer 0 to N-1 that corresponds to the tile's pieces that the player or CPU has chosen to move
def move_pieces(board,player,tile):
    
    other_player_row = 0 if player == 1 else 1
    
    # Get the number of pieces from the chosen tile
    pieces = board[player][tile]
    TilesPerPlayer=len(board[0])
    number_of_rows__pieces_were_distributed=0  

    # Set the chosen tile to 0 (empty it)
    board[player][tile] = 0
    
    # Split each individual piece and distribute them along the board 
    ones = pieces #Number of single pieces left to distribute
    while(ones>0):

        ##  RULE 1  ##
        #Distribute the pieces from left to right one at a time skipping the enemy's score tile
        #explanation:Player in the top row skips second rows last tile while player in the bottom
        #row skips the last tile of the top row

        #Player's row of tiles
        if (number_of_rows__pieces_were_distributed==0):
            for c in range(tile+1, TilesPerPlayer, 1):  #Distribute pieces starting after the tile that was emptied
                if ones > 0: #Are there any pieces left to distribute?
                    board[player][c] += 1
                    ones -= 1
                    last_row=player
                    last_col=c
            number_of_rows__pieces_were_distributed=1
        else:           
            for c in range(0, TilesPerPlayer, 1):  #Distribute pieces starting from the beginning of the row until the end
                if ones > 0:
                    board[player][c] += 1
                    ones -= 1
                    last_row=player
                    last_col=c
            
        #Opponents's row of tiles
        for c in range(0, TilesPerPlayer):  #Distribute in the first N-1 tiles
            if c == TilesPerPlayer-1:  # Skip opponent's score tile
                continue
            if ones > 0:
                board[other_player_row][c] += 1
                ones -= 1
                last_row=other_player_row
                last_col=c

        ##  RULE 2  ##
        #If the last piece is placed in an empty tile on the player's side, it is collected alongside any pieces in the tiles directly opposite
        #and are placed in the player's score-board tile unless theres nothing directly in the tile opposite to it
        if(board[last_row][last_col]==1 and last_col!=TilesPerPlayer-1 and player==last_row and board[last_row][last_col]+board[other_player_row][TilesPerPlayer-2-last_col]>1): 
            board[last_row][TilesPerPlayer-1]=board[last_row][TilesPerPlayer-1]+board[last_row][last_col]+board[other_player_row][TilesPerPlayer-2-last_col]
            board[last_row][last_col]=0 #Empty player's tile
            board[other_player_row][TilesPerPlayer-2-last_col]=0 #Empty opponent's tile opposite to the player's 
        
    ##  RULE 3: PLAY AGAIN
    #If the last piece distributed is placed in the player's scoreboard tile that he/she plays again
    if (pieces%(2*TilesPerPlayer-1)==TilesPerPlayer-1-tile):
        return board,player
        
    player=other_player_row  #if not play again then player is set to the other players number              
    return board,player

#This function takes into account the current state of the board and the player that is playing and returns the set of valid moves for that player
#A player can move pieces from non-empty tile in his row 
def valid_moves(board,player):
    possible_moves=[]     
    for i in range(len(board[0])-1):
        if(board[player][i]!=0):
            possible_moves.append(i)

    return possible_moves   

#Min-Max Algorithm for AI to find the best move in the Mancala Game
#This function considers the current state of the game (board), whose turn it is (player) and a specified depth of search ahead to determine the best available move
def minmax_mancala(board,player,depth,who_plays):

    best_move=-1
    #Search is over when the game is finished or the maximum search depth has been reached 
    if(sum(board[1][0:-1])==0 ): 
        best_score=board[1][-1]-sum(board[0][:])
        return best_score,best_move
    elif(sum(board[0][0:-1])==0):
        best_score=sum(board[1][:])-board[0][-1]
        return best_score,best_move
    elif(depth<=0):
        best_score=board[1][-1]-board[0][-1]
        return best_score,best_move

    if (who_plays[player]=="AI"):
        #Maximization
        best_score=-10000
        possible_moves=valid_moves(board,player)
        
        for move in possible_moves:
            #Copy current state of the board and use the copy foe the search purposes
            board_copy=copy.deepcopy(board)
            board_copy,player=move_pieces(board_copy,player,move)
            if(who_plays[player]=="AI"):
                points,_=minmax_mancala(board_copy,player,depth,who_plays) #When AI plays again the depth stays the same
            else:
                points,_=minmax_mancala(board_copy,player,depth-1,who_plays)
            #Save best move that corespons to the highest point gain
            if points>best_score:
                best_move=move
                best_score=points

            player=0 if who_plays[0]=="AI" else 1 #Change to player when ai's turn is complete

    else:
        #Minimization
        best_score=10000
        possible_moves=valid_moves(board,player)
        
        for move in possible_moves:
            board_copy=copy.deepcopy(board)
            board_copy,player=move_pieces(board_copy,player,move)
            if(who_plays[player]=="PLAYER"):
                points,_=minmax_mancala(board_copy,player,depth,who_plays) #When Player plays again the depth stays the same
            else:
                points,_=minmax_mancala(board_copy,player,depth-1,who_plays)
                
            if points<best_score:
                best_move=move
                best_score=points
                
            player=0 if who_plays[0]=="PLAYER" else 1 #Change to ai when player's turn is complete

    return best_score,best_move
