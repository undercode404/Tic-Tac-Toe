from check_win import check_for_win
from display_board import display_board
from sample_board import sample
from space_check import spaces
from marker import marker
from user_input import input_validification
from choose_player_turn import player_turn
from replay import replay

def main():           # if __name__ == "__main__"
    
    positions_available = [' '] * 10
    print("Welcome to Tic Tac Toe game.")
    print(''' This game is without GUI(Graphical User Interface) and will solely run on terminal.
    Some things need to kept in mind while playing this game and they are listed below :
    1.First you will be shown the Tic-Tac-toe board with their respective Index numbers, so you can get the idea how it looks.
    2.This game is made for user VS user and later the user VS computer feature will be added.
    3.After this, Users should decide who will be Player1 & 2 and the system will automatically decide who will go first.
    4.Now, specifically the player1 will be asked for marker i.e X or O.
    5.After that, each index input of the both players the tic-tac-toe board will be shown and
    6. Also simultaneously the previous board will be clean.
    7.Lastly, Enjoy the game!''')

    sample()

    turn = player_turn()
    print(turn +"has been selected by the system to go first.")
    player1_marker, player2_marker = marker()
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game = True
    else:
        game = False

    while game:

        if turn == 'player 1':


            player1_index = input_validification(positions_available)

            positions_available[player1_index]= player1_marker

            display_board(positions_available)


            if not spaces(positions_available):
                print(spaces(positions_available))
                print("The match has been a draw match.")
                break

            if check_for_win(positions_available,player1_marker):
                display_board(positions_available)
                print("Congratulations, Payer 1 you won the game!\nThank you for playing.")
                game = False

            else:
                turn = 'player 2'

        
        if turn == 'player 2':


            player2_index = input_validification(positions_available)

            positions_available[player2_index]= player2_marker

            display_board(positions_available)


            if spaces(positions_available)!=True:
                print(spaces(positions_available))
                print("The match has been a draw match.")
                break

            if check_for_win(positions_available,player2_marker):
                display_board(positions_available)
                print("Congratulations, Player 2 you won the game!\nThank you for playing.")
                game = False

            else:
                turn = 'player 1'



main()