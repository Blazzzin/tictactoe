from helpers import draw_board, check_turn, check_for_win
import os

# This is a dictionary. The value in the '' is what is used for the board
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

still_playing = True
complete = False
turn = 0
prev_turn = -1

while still_playing:
    # Reset the screen after each turn so it does not get confusing
    os.system('cls' if os.name == 'nt' else 'clear')

    draw_board(spots)

    # If an invalid turn occured, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn

    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")

    # Get input from the player
    choice = input()
    if choice == 'q':
        still_playing = False
    # Check if the player gave a number between 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if the spot has already been taken
        if not spots[int(choice)] in {"X", "O"}:
            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_for_win(spots):
        still_playing, complete = False, True

    if turn > 8:
        still_playing = False

# Print the resutls
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    # Tie
    print("The Game is Tied. No Winner!")