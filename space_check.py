from os import register_at_fork


def spaces(board):
    
    for i in range(1,10):
        if board[i] == ' ':
            return True
    else:
        return False