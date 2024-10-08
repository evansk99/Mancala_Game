#Create a board (matrix with 2 rows)containing 4 to 10 tiles with 2 to 6 pieces in each and 2 scoreboards
def create_board():
    tiles=int(input("Choose number of tiles per player (range 4-10):"))
    while(tiles<4 or tiles>10):
        tiles=int(input("Valid number of tiles per player 4-10:"))
    pieces=int(input("Choose number of pieces per tile (range 2-6):"))
    while(pieces<2 or pieces>6):
        pieces=int(input("Valid number of pieces per tile 2-6:"))
    element=[pieces]*(tiles)
    element.append(0)
    print(element)
    board=[element,element]
    print(board)
    return board

#Choose to play against a fellow player or against the CPU
def choose_opponent():
    choice=str(input("Press P for a Player vs Player game\nPress C to play against the computer:"))
    while(choice not in ['P','C']):
        choice=str(input("Player vs Player-->Type P\nPlayer vs Computer-->Type C\n"))
    opponent="PvP" if choice=='P' else 'CPU'
    return opponent

#Choose order of play    
def order_of_play_PvC():

    player=int(input("Type 1 to play first or 2 to play second:"))
    while(player not in [1,2]):
        player=int(input("Play first-->Type 1\nPlay second-->Type 2\n"))
    print("Player is located on the top row."
    who_plays=["PLAYER","AI"]
    skip_player=True if player==2 else False
    player=player-1
    return who_plays,player,skip_player   

#Choose the difficulty of the CPU opponent by setting the number of moves
#that the CPU will be looking ahead to find the best move (1,3,5 or 7)
def choose_difficulty():
    choice=int(input("Choose Difficulty:\nPress 1 for EASY\nPress 2 for MEDIUM\nPress 3 for HARD\nPress 4 for HELL\n"))
    while(choice not in [1,2,3,4]):
        choice=int(input("EASY-->Type 1\nMEDIUN-->Type 2\nHARD-->Type 3\nHELL-->Type 4\n"))
    difficulty=[1,3,5,7]
    return difficulty[choice-1]

#Player vs Player game choose who goes first (player 1 starts the game in the top row
def choose_side_PvP():
    print("Player 1 starts the game.")
    player=int(input("Type 1 to be Player 1 on the Top Row or 2 to be Player 2 on Bottom Row:"))
    while(player not in [1,2]):
        player=int(input("Player 1-->Type 1\nPlayer 2-->Type 2\n"))
    return player   
