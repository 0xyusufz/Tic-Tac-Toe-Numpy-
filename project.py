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

print_board(board)

