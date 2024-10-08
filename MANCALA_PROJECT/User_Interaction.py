from Play_Game import valid_moves

#Players choose the next move they want to play out of a set of valid moves.
def choose_move(board,player):
    tile=int(input("Choose a NON-EMPTY tile from your row:"))
    while(tile>=int((len(board[0])-1)) or tile<0 or board[player][tile]==0):
        print("Invalid move")
        print("Tile Number must be from 0 to " + str(len(board[0])-2) + " and it must be a NON-EMPTY tile:")
        possible_moves=valid_moves(board,player)
        print("Valid Moves:",possible_moves)
        tile=int(input("Your Choice:"))
    return tile

#Show current state of the board in a player vs player or player vs computer game
def show_board(board,opponent,skip_opponent): 
    #Number of playable tiles
    tiles=int(len(board[0]))-1

    #Print tile number for player 1
    print(5*' ',end='')
    for tile_number in range(tiles-1,-1,-1):
        print(str(tile_number),end='  ')
        
    print(5*' ',end='\n')

    #Top seperator
    print('+'+3*'-'+tiles*'+--'+'+'+3*'-', end='+\n')  
    
    #Print player 1 tiles from right to left (order of play)
    if(opponent=='PvP'):
        print('|P1 |', end='')
    else:
        if(skip_opponent==False):
            print('|YOU|', end='')
        else:
            print('|CPU|', end='')
    for index in range(tiles-1, -1, -1):
        print(' '+str(board[0][index])+'|', end='') if(len(str(board[0][index]))==1) else print(str(board[0][index])+'|', end='') #fitting number of pieces in tiles
    print('   | <--')  

    #Print players scores 
    print('|',str(board[0][-1]),end='')
    print(' +',end='') if(len(str(board[0][-1]))==1) else print('+',end='')
    print(tiles*'--+',end=' ')
    print(str(board[1][-1]),end='')
    print(' +',end='\n') if(len(str(board[1][-1]))==1) else print('+',end='\n')
    
    #Print player 2 tiles from left to right (order of play)
    print('|   |', end='')
    for index in range(0, tiles, 1):
        print(' '+str(board[1][index])+'|', end='') if(len(str(board[1][index]))==1) else print(str(board[1][index])+'|', end='')          
    if(opponent=='PvP'):
        print(' P2| -->', end='\n')
    else:
        if(skip_opponent==False):
            print('CPU| -->', end='\n')
        else:
            print('YOU| -->', end='\n')
            
    #Bottom seperator
    print('+'+3*'-'+tiles*'+--'+'+'+3*'-', end='+\n')  

    #Print tile number for player 2
    print(5*' ',end='')
    for tile_number in range(0,tiles,1):
        print(str(tile_number),end='  ')
        
    print(5*' ',end='\n')

#This function uses current state of the game (board) to determine if the game is finished (playing=True/False)
#That is the case when all the playable tiles of either player are empty.
def check_if_end_game(board,playing):
    if(sum(board[0][0:-1])==0 or sum(board[1][0:-1])==0):
        playing=False
    return playing

#This function declares the winner when the game is complete and prints out the winner!
#It compares the scores of each player taking into account if there are spare pieces in either players row
def results(board,skip_player,opponent):
    print("GAME IS OVER")
    if opponent=='CPU':
        if(sum(board[0])>sum(board[1])):
            print("PLAYER IS VICTORIOUS!")
        elif(sum(board[0])<sum(board[1])):
            print("COMPUTER IS VICTORIOUS!")
        else:
            print("IT IS A TIE!")
        if(skip_player==False):
            print("FINAL SCORE: " + str(sum(board[0])) + " - " + str(sum(board[1]))) 
        else:
            print("FINAL SCORE: " + str(sum(board[1])) + " - " + str(sum(board[0])))
    else:
        if(sum(board[0])>sum(board[1])):
            print("PLAYER 1 IS VICTORIOUS!")
        elif(sum(board[0])<sum(board[1])):
            print("PLAYER 2 IS VICTORIOUS!")
        else:
            print("IT IS A TIE!")
        print("FINAL SCORE: " + str(sum(board[0])) + " - " + str(sum(board[1])))
