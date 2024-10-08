from Game_Settings import *
from Play_Game import *
from User_Interaction import *
import copy

def main():
    playing=True #Game ongoing as long as playing=True
    print("Welcome to MANCALA!")
    skip_opponent=False #In player vs cpu mode it allows cpu to play first (when True)

    #GAME SETTINGS
    board=create_board()
    opponent=choose_opponent()
    if(opponent=='PvP'):
        player=choose_side_PvP()-1
    else:
        who_plays,player,skip_player=order_of_play_PvC()
        MAX_Depth=choose_difficulty() #Set search algorithm depth (number of moves cpu calculates ahead
        #MAX_Depth=_ #Set difficulty manually
    show_board(board,opponent,skip_opponent) #Displays current board state

    #PLAY THE GAME
    while(playing):
        
        if(opponent=='PvP'):
            print("IT IS PLAYER " + str(player+1) + " TURN!")
            print(board)
            tile=choose_move(board,player)
            board,player=move_pieces(board,player,tile)
            show_board(board,opponent,skip_opponent)
        elif(opponent=='CPU'):
            print("IT IS " + who_plays[player] + "'s TURN!")
            if(who_plays[player]=="PLAYER"):
                tile=choose_move(board,player)
                board,player=move_pieces(board,player,tile)
            else:
                _,best_move=minmax_mancala(board,player,MAX_Depth,who_plays)
                board,player=move_pieces(board,player,best_move)
            show_board(board,opponent,skip_opponent)
        playing=check_if_end_game(board,playing) #Check if game is finished

    #FINAL RESULT
    results(board,skip_player,opponent)

     
if __name__ == "__main__":
    main()
