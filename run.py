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


def rand_row(board_size):
    """
    creates a list of randomly selected row numbers
    for the positions of the targets
    """
    rows = []
    target_row = 0
    for _ in range(4):
        target_row = randint(0, board_size - 1)
        rows.append(target_row)
    return rows


def rand_col(board_size):
    """
    creates a list of randomly selected column
    numbers for the positions of the targets
    """
    cols = []
    target_col = 0
    for _ in range(4):
        target_col = randint(0, board_size - 1)
        cols.append(target_col)
    return cols


"""
Loops through the random generated x and y
values and appends them as a tuple to a list
of target coordinates
"""
target_rows = rand_row(5)
target_columns = rand_col(5)
for x, y in zip(target_columns, target_rows):
    if (x, y) not in targets_list:
        targets_list.append((x, y))

print(targets_list)


def print_board(board_size):
    """
    prints the board for the user to play against
    """
    global board
    board = []

    for _ in range(board_size):
        board.append(['.'] * board_size)

    for row in board:
        print("  ".join(row))


print_board(5)


"""
Set the number of shots the user will take and set
the number of hits to 0 at the beginning of the game
"""
max_shots = 8
shot = 0
hits = 0


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
