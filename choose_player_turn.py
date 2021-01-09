import random 

def player_turn():

    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'