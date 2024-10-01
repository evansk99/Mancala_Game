from User_Interaction import *
from move_pieces import move_pieces

playing=True
print("Welcome to MANCALA!")
board=initialize_board()
player=choose_player()-1

while(playing):
    print("IT IS PLAYER " + str(player+1) + " TURN!")
    board,player=move_pieces(board,player)
    playing=end_game(board,playing)
results(board)
