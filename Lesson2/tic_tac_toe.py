def main():
    scores = {'Player 1':0, "Player 2":0}
    print(scores['Player 1'])
    scores['Player 1'] += 1
    print(scores)

def print_scores(scores):
    print(f"Player 1 score: {scores['Player 1']}\n\
Player 2 score: {scores['Player 2']}")

def choice():

main()
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

while True:
    play = input("Would you like to play tic tac toe? 1) Yes, 2) No ")
    try:
        if play == 1:
            row1 = int(input("What row would you like to enter (1) top, 2) middle, 3) bottom): "))
            column1= int(input("What column would you like to use (1) left, 2) middle, 3) right"))
            board[1][1] = 'X'
        else:
            break
    except ValueError:
        print("Invalid Input")
        print(" ")
        continue

