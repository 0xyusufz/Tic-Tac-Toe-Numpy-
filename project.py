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

current = 1
print("Welcome to Tic-Tac-Toe")
print_board(board)

while True:
    if current == 1:
        player = "X"
    else:
        player = "O"
    print(f"current chance : {player}")
    try:
        row = int(input(f"{player}: enter the row b/w 0 to 2: "))
        if row >2 or row < 0:
            raise Exception("please enter b/w 0 to 2: ")
        col = int(input(f"{player}: enter the column b/w 0 to 2: "))
        if col >2 or row < 0:
            raise Exception("please enter b/w 0 to 2: ")
    except ValueError:
        print("please enter th number only \n")
        continue
    except Exception as e:
        print(f"something went wrong \n{e} \n")
        continue
    
    if board[row,col] != 0:
        print("cell already taken")
        print_board(board)
        continue
    board[row,col] = current
    print_board(board)
    
    result = check_winner(board)
    if result is not None:
        if result == "DRAW":
            print("Match Draw")
        else:
            print(f"{result}: wins")
        break
    if current == 1:
        current = -1
        print(f"{current} from if")
    else:
        current = 1



