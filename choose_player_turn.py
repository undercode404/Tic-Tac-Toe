import random 

def player_turn():

    if random.randint(1,2) == 1:
        return 'player 1'
    else:
        return 'player 2'