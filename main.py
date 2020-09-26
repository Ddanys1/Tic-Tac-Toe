# ____________Global Variables___________________
board = ['blank', "-", "-", "-", "-", "-", "-", "-", "-", "-"]
current_player = ""
game_on = True


# Game logic:
# Select first player's mark
# Select a position to place mark on board
# Check if player have won
# Check if it's a tie
# Jump to next player
# Repeat
def game_play():
    global game_on
    global current_player
    select_player()
    while game_on:
        if current_player == "X":
            player_choice()
            game_win_conditions(board)
            current_player = "O"
        elif current_player == "O":
            player_choice()
            game_win_conditions(board)
            current_player = "X"


# Prints a game board (position [0] is blank)
def board_print(board):
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])


# Lets first player to select his marker to X or O
def select_player():
    global current_player
    asking = True
    while asking:
        marker = input("Please select your marker X or O: ").upper()
        if marker == "X" or marker == "O":
            current_player = marker
            asking = False
        else:
            print("Selected character is invalid")


# Lets current player to select an empty position to place its marker
def player_choice():
    global board
    asking = True
    while asking:
        marker = int(input("Please select a position from 1 to 9 to place your marker: "))
        if board[marker] == '-':
            board[marker] = current_player
            board_print(board)
            asking = False
        else:
            print("Position is already taken")


# Checks if current player have won and calls function to check if it's a tie
def game_win_conditions(board):
    global current_player
    global game_on
    if board[2] == board[1] == board[3] != "-" or board[4] == board[5] == board[6] != "-" or board[7] == board[8] == \
            board[9] != "-" or board[1] == board[4] == board[7] != "-" or board[1] == board[4] == board[7] != "-" or \
            board[2] == board[5] == board[8] != "-" or board[3] == board[6] == board[9] != "-" or \
            board[1] == board[5] == board[9] != "-" or board[7] == board[5] == board[3] != "-":
        print(f"winner is {current_player}")
        game_on = False
    else:
        game_tie(board)


# Checks if it's a tie
def game_tie(board):
    global current_player
    global game_on
    if "-" not in board:
        print("It is a tie!")
        game_on = False


game_play()
