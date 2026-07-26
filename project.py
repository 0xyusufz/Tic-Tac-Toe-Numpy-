import numpy as np

board = np.zeros([3,3],dtype=int)

def print_board(b):
    symbols = {0: " ",1:"X",-1:"O"}
    for r in range(3):
        row= " | ".join([symbols[val] for val in b[r]])
        print(" "+row)
        if r < 2:
            print("---+---+---")
    print()

def check_winner(b):
    if 3 in np.sum(b,axis= 1) or 3 in np.sum(b,axis = 0) or 3 == np.trace(b) or 3 == np.trace(np.fliplr(b)):
        return "X"
    if -3 in np.sum(b,axis= 1) or -3 in np.sum(b,axis = 0) or -3 == np.trace(b) or -3 == np.trace(np.fliplr(b)):
        return "O"
    if not 0 in b:
        return "DRAW"
    return None


print_board(board)

