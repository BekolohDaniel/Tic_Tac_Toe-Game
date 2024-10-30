##Tic_Tac_Toe Game
import random

#  A dictionary for the game's moves
game_moves = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}

#  Names of the players
player1 = 'Human'
player2 = 'Computer'


#  Current player
def current_player_name():
    current_player = player1
    if current_player == player1:
        return player1
    else:
        return player2


# Grid Setup
def grid_setup():
    print('------------')
    print(' ' + game_moves[1] + ' | ' + game_moves[2] + ' | ' + game_moves[3])
    print('------------')
    print(' ' + game_moves[4] + ' | ' + game_moves[5] + ' | ' + game_moves[6])
    print('------------')
    print(' ' + game_moves[7] + ' | ' + game_moves[8] + ' | ' + game_moves[9])
    print('------------')

# number of times a player has played
player1_move , player2_move = 0, 0


# Player move
def player_move():
    global player1_move
    mover = current_player_name()
    print(mover + "'s turn")
    move = int(input("Enter a number: "))
    if game_moves[move] == ' ':
        game_moves[move] = 'X'
    else:
        print("Invalid move. Try again.")
        player_move()
    if mover == player1:
        mover = player2
    player1_move += 1
    return mover


# Computer move
def computer_move():
    global player2_move
    rand_num = random.randint(1, 9)
    mover = player2
    print(mover + "'s turn")
    move = rand_num
    print(move)
    if game_moves[move] == ' ':
        game_moves[move] = 'O'
    else:
        print("Invalid move. Try again.")
        computer_move()
    if mover == player2:
        mover = player1
    player2_move += 1
    return mover


# Check if user wins
def check_user_win():
    # Checks if Player1 is the winner
    if game_moves[1] == 'X' and game_moves[2] == 'X' and game_moves[3] == 'X':
        return True
    elif game_moves[4] == 'X' and game_moves[5] == 'X' and game_moves[6] == 'X':
        return True
    elif game_moves[7] == 'X' and game_moves[8] == 'X' and game_moves[9] == 'X':
        return True
    elif game_moves[1] == 'X' and game_moves[4] == 'X' and  game_moves[7] == 'X':
        return True
    elif game_moves[2] == 'X' and game_moves[5] == 'X' and game_moves[8] == 'X':
        return True
    elif game_moves[3] == 'X' and game_moves[6] == 'X' and game_moves[9] == 'x':
        return True

    elif game_moves[1] == 'X' and game_moves[5] == 'X' and game_moves[9] == 'X':
        return True
    elif game_moves[3] == 'X' and game_moves[5] == 'X' and game_moves[7] == 'X':
        return True

    else:
        return False

# Checks if computer win
def check_computer_win():
    # Checks if player2 computer is the winner
    if game_moves[1] == 'O' and game_moves[2] == 'O' and game_moves[3] == 'O':
        return True
    elif game_moves[4] == 'O' and game_moves[5] == 'O' and game_moves[6] == 'O':
        return True
    elif game_moves[7] == 'O' and game_moves[8] == 'O' and game_moves[9] == 'O':
        return True
    elif game_moves[1] == 'O' and game_moves[4] == 'O' and game_moves[7] == 'O':
        return True
    elif game_moves[2] == 'O' and game_moves[5] == 'O' and game_moves[8] == 'O':
        return True
    elif game_moves[3] == 'O' and game_moves[6] == 'O' and game_moves[9] == 'O':
        return True

    elif game_moves[1] == 'O' and game_moves[5] == 'O' and game_moves[9] == 'O':
        return True
    elif game_moves[3] == 'O' and game_moves[5] == 'O' and game_moves[7] == 'O':
        return True

    else:
        return False


# Check for tie
def check_tie():
    for key in game_moves:
        if game_moves[key] == ' ':
            return False
    return True


# Play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 = X, Player 2 = O")

    while True:
        player_move()
        grid_setup()
        if check_user_win():
            print(current_player_name() + ' Wins!')
            break
        elif check_tie():
            print("Tie game!")
            break
        computer_move()
        grid_setup()
        if check_computer_win():
            print(player2 + ' Wins!')
            break
        elif check_tie():
            print("Tie game!")
            break


play_game()
