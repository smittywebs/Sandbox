
def did_I_win_2_down(player, board):
    #did_win = player == board[0][2] and \
    #          player == board[1][2] and \
    #          player == board[2][2]
    did_win = True
    for i in range(3):
        did_win &= player == board[i][2]
        
    return did_win

def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])

def main():
    boards = [ [["x", "o", "o"]] * 3, \
               [["x", "o", "x"], ["o"] * 3, ["o", "x", "o"]], \
               [['o', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'o']], \
               [["o", "o", "x"]] * 3 ]
    for b in boards:
        print_2D_board(b)
        print("x won?", did_I_win_2_down("x", b))
        print("o won?", did_I_win_2_down("o", b))

if __name__ == "__main__":
    main()