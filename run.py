# Save Space battleships style game

from random import randint

# Title welcoming player to game
print(
    "✮ Welcome ✮\nYour mission, should you choose to accept it, is to\n"
    +
    """
░██████╗░█████╗░██╗░░░██╗███████╗  ░██████╗██████╗░░█████╗░░█████╗░███████╗
██╔════╝██╔══██╗██║░░░██║██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
╚█████╗░███████║╚██╗░██╔╝█████╗░░  ╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░
░╚═══██╗██╔══██║░╚████╔╝░██╔══╝░░  ░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░
██████╔╝██║░░██║░░╚██╔╝░░███████╗  ██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝"""
    +
    "\n\nThere are 4 enemy spacecraft somewhere around us.\n"
    +
    "Shoot them with your lazer to eliminate the threat. You have 8 chances.\n"
)


targets_list = []


def generate_targets_list(rows, cols, num_of_targets):
    """
    Randomly generate a list of target coordinates
    """
    targets_list = []
    added_targets = 0
    while added_targets < num_of_targets:
        target_col_idx = randint(0, cols-1)
        target_row_idx = randint(0, rows-1)
        position = [target_col_idx, target_row_idx]
        if position not in targets_list:
            added_targets = added_targets + 1
            targets_list.append(position)
    print(targets_list)
    return targets_list


def initialise_board(rows, cols):
    """
    Initialises the game board
    """
    global board
    board = []

    for _ in range(cols):
        board.append(['.'] * rows)


def print_board():
    """
    Prints the game board for the user to play against
    """
    global board

    for row in board:
        print("  ".join(row))


def ask_to_play_again():
    """
    At end of the game ask user if they want to play again
    """
    choice = input("Do you want to play again? Type Y/N")
    if choice == 'Y':
        init_game()
    else:
        print("Thanks for playing Save Space!")


def start_game(rows, cols, num_of_targets, total_num_of_guesses):
    """
    Function to run the gameplay until either all targets are
    hit or all guesses have been made
    """
    targets_list = generate_targets_list(rows, cols, num_of_targets)

    user_guesses = []

    shots = 0
    hits = 0

    while hits < num_of_targets and shots < total_num_of_guesses:
        print(f'Shot number {shots + 1}')

        user_guess = get_user_guesses()
        print(user_guess, user_guesses)
        if user_guess in user_guesses:
            print('You already shot there! Try again')
        elif user_guess in targets_list:
            user_guesses.append(user_guess)
            shots += 1
            board[user_guess[0]][user_guess[1]] = 'X'
            hits += 1
            print('Well done! You hit an enemy spacecraft')
        else:
            user_guesses.append(user_guess)
            shots += 1
            board[user_guess[0]][user_guess[1]] = '-'
            print('You missed this time')

        print_board()

    if hits == num_of_targets:
        print("Congratulations! You Saved Space!")
    else:
        print(f'Game over! You hit {hits} enemy spacecraft')

    ask_to_play_again()


def take_col_input_guess():
    user_xstr = input('\nGuess an x coordinate between 1 and 5: ')
    if user_xstr not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        return take_col_input_guess()
    else:
        return int(user_xstr) - 1


def take_row_input_guess():
    user_ystr = input('\nGuess an y coordinate between 1 and 5: ')
    if user_ystr not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        return take_row_input_guess()
    else:
        return int(user_ystr) - 1


def get_user_guesses():
    """
    request user to input a row and column value
    check if input is valid and add to list of guesses
    """
    col = take_col_input_guess()
    row = take_row_input_guess()

    return [col, row]
