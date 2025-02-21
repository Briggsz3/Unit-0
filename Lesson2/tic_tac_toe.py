def main():
    scores = {'Player 1':0, "Player 2":0}
    print(scores['Player 1'])
    scores['Player 1'] += 1
    print(scores)

def print_scores(scores):
    print(f"Player 1 score: {scores['Player 1']}\n\
Player 2 score: {scores['Player 2']}")
    
def check_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True
    


# ask user if they want to play again 
# ask user where they want to put their X or O
# have a funcion that puts takes the user input and places it on the board
# Function that analyzes if there is a win (8 different ways of winning tic tac toe) (3 vertical, 3 horizantal and 2 diagonal)
# if there is a win shoot it back up to the top to see if the person wants to play again
# Use a try except to not accpet any invalid inputs
# Use a list and a if ____ in ____ to find out if the input has already been used
# make each available space a number ex: spc1
# Could make a table of all spaces, would make sense but might be a little difficult.
# assign each space a number and have the number be a variable that gets filled with player one.
# Look at jeopardy game bc there was a good system of not trapping user in a column if they already answered a question. 
# turn = 0 and if turn == 9 then end game
board_list = []
p1_score = 0
p2_score = 0
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
while True:
    play = int(input("Would you like to play tic tac toe? 1) Yes, 2) No "))
    print(" ")
    try:
        if play == 1:
            row1 = int(input("Player 1 (X) what row would you like to enter (1 top, 2 middle, 3 bottom): "))
            try: 
                column1= int(input("Player 1 (X) what column would you like to use (1) left, 2) middle, 3) right: "))
                try :
                    if row1 == 1:
                        if column1 == 1:
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
                                continue
                            elif board1[0][0] == 'X' and board1[1][1] == 'X' and board1[2][2] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                            elif board1[0][0] == 'X' and board1[1][0] == 'X' and board1[2][0] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                        if column1 == 2:
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
                            elif board1[0][1] == 'X' and board1[1][1] == 'X' and board1[2][1] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                        if column1 == 3:
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
                            elif board1[0][2] == 'X' and board1[1][1] == 'X' and board1[2][0] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][2] == 'X' and board1[2][2] == 'X' and board1[1][2] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                    elif row1 == 2:
                        if column1 == 1:
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
                            elif board1[1][0] == 'X' and board1[2][0] == 'X' and board1[0][0] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column1 == 2:
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
                            elif board1[2][1] == 'X' and board1[1][1] == 'X' and board1[0][1] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][0] == 'X' and board1[1][1] == 'X' and board1[2][2] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[2][0] == 'X' and board1[1][1] == 'X' and board1[0][2] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column1 == 3:
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
                            elif board1[1][2] == 'X' and board1[2][2] == 'X' and board1[0][2] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                    elif row1 == 3:
                        if column1 == 1:
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
                            elif board1[2][0] == 'X' and board1[0][2] == 'X' and board1[1][1] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][0] == 'X' and board1[1][0] == 'X' and board1[2][0] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column1 == 2:
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
                            elif board1[2][0] == 'X' and board1[2][2] == 'X' and board1[2][1] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column1 == 3:
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
                            elif board1[0][0] == 'X' and board1[2][2] == 'X' and board1[1][1] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[1][2] == 'X' and board1[2][2] == 'X' and board1[0][2] == 'X':
                                print("Player One wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        else:
                            print(" ")
                            print("Invalid input")
                            print(" ")   
                    else:
                        print(" ")
                        print("Invalid input")
                        print(" ")
                except ValueError:
                    print("Invalid Input")
                    print(" ")
                    continue
            except ValueError:
                print("Invalid Input")
                print(" ")
                continue
            row2 = int(input("Player 2 (O) what row would you like to enter (1 top, 2 middle, 3 bottom): "))
            try: 
                column2= int(input("Player 2 (O) what column would you like to use (1) left, 2) middle, 3) right: "))
                try :
                    if row2 == 1:
                        if column2 == 1:
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
                            elif board1[0][0] == 'O' and board1[1][1] == 'O' and board1[2][2] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][0] == 'O' and board1[1][0] == 'O' and board1[2][0] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column2 == 2:
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
                            elif board1[0][1] == 'O' and board1[1][1] == 'O' and board1[2][1] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column2 == 3:
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
                            elif board1[0][2] == 'O' and board1[1][1] == 'O' and board1[2][0] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][2] == 'O' and board1[2][2] == 'O' and board1[1][2] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                    elif row2 == 2:
                        if column2 == 1:
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
                            elif board1[1][0] == 'O' and board1[2][0] == 'O' and board1[0][0] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column2 == 2:
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
                            elif board1[2][1] == 'O' and board1[1][1] == 'O' and board1[0][1] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][0] == 'O' and board1[1][1] == 'O' and board1[2][2] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[2][0] == 'O' and board1[1][1] == 'O' and board1[0][2] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column2 == 3:
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
                            elif board1[1][2] == 'O' and board1[2][2] == 'O' and board1[0][2] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                    elif row2 == 3:
                        if column2 == 1:
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
                            elif board1[2][0] == 'O' and board1[0][2] == 'O' and board1[1][1] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[0][0] == 'O' and board1[1][0] == 'O' and board1[2][0] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column2 == 2:
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
                            elif board1[2][0] == 'O' and board1[2][2] == 'O' and board1[2][1] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        if column2 == 3:
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
                            elif board1[0][0] == 'O' and board1[2][2] == 'O' and board1[1][1] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif board1[1][2] == 'O' and board1[2][2] == 'O' and board1[0][2] == 'O':
                                print("Player 2 wins")
                                p1_score = p1_score +1
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                            elif check_board_full(board1):
                                print("It's a draw")
                                print(f"Player 1: {p1_score}  Player 2: {p2_score}")
                                continue
                        else:
                            print(" ")
                            print("Invalid input")
                            print(" ")   
                    else:
                        print(" ")
                        print("Invalid input")
                        print(" ")
                except ValueError:
                    print("Invalid Input")
                    print(" ")
                    continue
            except ValueError:
                print("Invalid Input")
                print(" ")
                continue
        else:
            break
    except ValueError:
        print("Invalid Input")
        print(" ")
        continue





