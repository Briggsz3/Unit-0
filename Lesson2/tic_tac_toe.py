# create an end game function that asks if you want to play again
# put that function at all winning situatios
board_list = []
p1_score = 0
p2_score = 0
board1 = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
def new_board(board1,board_list):
    board_list.clear()
    board1 = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
        ]


def board():
    for i in board1:
        print(i, end=" ")
        print()
    return(" ")

def check_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

while True:
    play = int(input("Would you like to play tic tac toe? 1) Yes, 2) No "))
    print(" ")
    try:
        if play == 1:
            while True:
                space1 = int(input("Player 1 (X) what space would you like to use (1) top left, 2) top middle, 3) top right, 3) middle left etc...: "))
                print(" ")
                try :
                    if space1 == 1:
                        if 11 in board_list:
                            print("This square is full")
                            continue
                        board1[0][0] = 'X'
                        board_list.append(11)
                        print(board())
                        if board1[0][0] == 'X' and board1[0][2] == 'X' and board1[0][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][0] == 'X' and board1[1][1] == 'X' and board1[2][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][0] == 'X' and board1[1][0] == 'X' and board1[2][0] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 2:
                        if 12 in board_list:
                            print("This square is full")
                            continue
                        board1[0][1] = 'X'
                        board_list.append(12)
                        print(board())
                        if board1[0][0] == 'X' and board1[0][2] == 'X' and board1[0][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][1] == 'X' and board1[1][1] == 'X' and board1[2][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 3:
                        if 13 in board_list:
                            print("This square is full")
                            continue
                        board1[0][2] = 'X'
                        board_list.append(13)
                        print(board())
                        if board1[0][0] == 'X' and board1[0][1] == 'X' and board1[0][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][2] == 'X' and board1[1][1] == 'X' and board1[2][0] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][2] == 'X' and board1[2][2] == 'X' and board1[1][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 4:
                        if 21 in board_list:
                            print("This square is full")
                            continue
                        board1[1][0] = 'X'
                        board_list.append(21)
                        print(board())
                        if board1[1][0] == 'X' and board1[1][1] == 'X' and board1[1][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[1][0] == 'X' and board1[2][0] == 'X' and board1[0][0] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 5:
                        if 22 in board_list:
                            print("This square is full")
                            continue
                        board1[1][1] = 'X'
                        board_list.append(22)
                        print(board())
                        if board1[1][0] == 'X' and board1[1][1] == 'X' and board1[1][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[2][1] == 'X' and board1[1][1] == 'X' and board1[0][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][0] == 'X' and board1[1][1] == 'X' and board1[2][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[2][0] == 'X' and board1[1][1] == 'X' and board1[0][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 6:
                        if 23 in board_list:
                            print("This square is full")
                            continue
                        board1[1][2] = 'X'
                        board_list.append(22)
                        print(board())
                        if board1[1][0] == 'X' and board1[1][2] == 'X' and board1[1][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[1][2] == 'X' and board1[2][2] == 'X' and board1[0][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 7:
                        if 31 in board_list:
                            print("This square is full")
                            continue
                        board1[2][0] = 'X'
                        board_list.append(31)
                        print(board())
                        if board1[2][0] == 'X' and board1[2][2] == 'X' and board1[2][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[2][0] == 'X' and board1[0][2] == 'X' and board1[1][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][0] == 'X' and board1[1][0] == 'X' and board1[2][0] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 8:
                        if 32 in board_list:
                            print("This square is full")
                            continue
                        board1[2][1] = 'X'
                        board_list.append(32)
                        print(board())
                        if board1[2][1] == 'X' and board1[1][1] == 'X' and board1[0][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[2][0] == 'X' and board1[2][2] == 'X' and board1[2][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    elif space1 == 9:
                        if 33 in board_list:
                            print("This square is full")
                            continue
                        board1[2][2] = 'X'
                        board_list.append(33)
                        print(board())
                        if board1[2][0] == 'X' and board1[2][2] == 'X' and board1[2][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[0][0] == 'X' and board1[2][2] == 'X' and board1[1][1] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif board1[1][2] == 'X' and board1[2][2] == 'X' and board1[0][2] == 'X':
                            print("Player One wins")
                            p1_score = p1_score +1
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                        elif check_board_full(board1):
                            print("It's a draw")
                            print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            print(" ")
                            new_board(board1,board_list)
                            continue
                    else:
                        print(" ")
                        print("Invalid input")
                        print(" ")
                except ValueError:
                    print("Invalid Input")
                    print(" ")
                    continue
                while True:
                    try: 
                        space2 = int(input("Player 2 (O) what space would you like to use (1) top left, 2) top middle, 3) top right, 3) middle left etc...: "))
                        print(" ")
                        try :
                            if space2 == 1:
                                if 11 in board_list:
                                    print("This square is full")
                                    continue
                                board1[0][0] = 'O'
                                board_list.append(11)
                                print(board())
                                if board1[0][0] == 'O' and board1[0][2] == 'O' and board1[0][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][0] == 'O' and board1[1][1] == 'O' and board1[2][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][0] == 'O' and board1[1][0] == 'O' and board1[2][0] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 2:
                                if 12 in board_list:
                                    print("This square is full")
                                    continue
                                board1[0][1] = 'O'
                                board_list.append(12)
                                print(board())
                                if board1[0][0] == 'O' and board1[0][2] == 'O' and board1[0][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][1] == 'O' and board1[1][1] == 'O' and board1[2][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 3:
                                if 13 in board_list:
                                    print("This square is full")
                                    continue
                                board1[0][2] = 'O'
                                board_list.append(13)
                                print(board())
                                if board1[0][0] == 'O' and board1[0][1] == 'O' and board1[0][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][2] == 'O' and board1[1][1] == 'O' and board1[2][0] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][2] == 'O' and board1[2][2] == 'O' and board1[1][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 4:
                                if 21 in board_list:
                                    print("This square is full")
                                    continue
                                board1[1][0] = 'O'
                                board_list.append(21)
                                print(board())
                                if board1[1][0] == 'O' and board1[1][1] == 'O' and board1[1][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[1][0] == 'O' and board1[2][0] == 'O' and board1[0][0] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 5:
                                if 22 in board_list:
                                    print("This square is full")
                                    continue
                                board1[1][1] = 'O'
                                board_list.append(22)
                                print(board())
                                if board1[1][0] == 'O' and board1[1][1] == 'O' and board1[1][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[2][1] == 'O' and board1[1][1] == 'O' and board1[0][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][0] == 'O' and board1[1][1] == 'O' and board1[2][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[2][0] == 'O' and board1[1][1] == 'O' and board1[0][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            if space2 == 6:
                                if 23 in board_list:
                                    print("This square is full")
                                    continue
                                board1[1][2] = 'O'
                                board_list.append(22)
                                print(board())
                                if board1[1][0] == 'O' and board1[1][2] == 'O' and board1[1][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[1][2] == 'O' and board1[2][2] == 'O' and board1[0][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 7:
                                if 31 in board_list:
                                    print("This square is full")
                                    continue
                                board1[2][0] = 'O'
                                board_list.append(31)
                                print(board())
                                if board1[2][0] == 'O' and board1[2][2] == 'O' and board1[2][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[2][0] == 'O' and board1[0][2] == 'O' and board1[1][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][0] == 'O' and board1[1][0] == 'O' and board1[2][0] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 8:
                                if 32 in board_list:
                                    print("This square is full")
                                    continue
                                board1[2][1] = 'O'
                                board_list.append(32)
                                print(board())
                                if board1[2][1] == 'O' and board1[1][1] == 'O' and board1[0][1] == 'OX':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[2][0] == 'O' and board1[2][2] == 'O' and board1[2][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            elif space2 == 9:
                                if 33 in board_list:
                                    print("This square is full")
                                    continue
                                board1[2][2] = 'O'
                                board_list.append(33)
                                print(board())
                                if board1[2][0] == 'O' and board1[2][2] == 'O' and board1[2][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[0][0] == 'O' and board1[2][2] == 'O' and board1[1][1] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif board1[1][2] == 'O' and board1[2][2] == 'O' and board1[0][2] == 'O':
                                    print("Player 2 wins")
                                    p1_score = p1_score +1
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                elif check_board_full(board1):
                                    print("It's a draw")
                                    print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                    print(" ")
                                    new_board(board1,board_list)
                                    continue
                                break
                            else:
                                print(" ")
                                print("Invalid input")
                                print(" ")
                        except ValueError:
                            print("Invalid Input")
                            print(" ")
                            continue
                    except ValueError:
                        print(" ")
                        print("Invalid Input")
                        print(" ")
                        continue
    except ValueError:
        print("Invalid Input")
        print(" ")
        continue
