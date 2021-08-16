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
    "Shoot them with your lazer to eliminate the threat.\n"
)

# user chooses difficulty

# board = []

# # board size 5
# for i in range(0, 5):
#     board.append(['.'] * 5)


def print_board(board_size):
    """
    prints the board for the user to play against
    """
    global board
    board = []

    for _ in range(board_size):
        board.append(['.'] * board_size)

    for row in board:
        print(" ".join(row))


print_board(5)

targets_list = []


def rand_row(board_size):
    """
    creates a list of randomly selected row numbers
    for the positions of the targets
    """
    rows = []
    target_row = 0
    for _ in range(4):
        target_row = randint(0, board_size)
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
        target_col = randint(0, board_size)
        cols.append(target_col)
    return cols


target_rows = rand_row(5)
target_columns = rand_col(5)
for x, y in zip(target_columns, target_rows):
    if (x, y) not in targets_list:
        targets_list.append((x, y))

print(targets_list)


def get_user_guesses():
    """
    request user to input a row and column value
    check if input is valid
    """
    user_x = input('Guess an x coordinate between 1 and 5: ')
    while user_x not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        user_x = input('Guess a column between 1 and 5: ')

    user_y = input('Guess a y coordinate between 1 and 5: ')
    while user_y not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        user_y = input('Guess a row between 1 and 5: ')

    return int(user_x) - 1, int(user_y) - 1


# get_user_guesses()


user_guesses = []


def guess_row():
    """
    Takes user input for y coordinate value and
    appends it to a list of y values, taking into
    account zero-based indexing
    """
    guess_rows = []
    user_ystr = input('Guess a y coordinate between 1 and 5: ')
    user_y = int(user_ystr) - 1
    guess_rows.append(user_y)
    return guess_rows


def guess_column():
    """
    Takes user input for x coordinate value and
    appends it to a list of x values, taking into
    account zero-based indexing
    """
    guess_columns = []
    user_xstr = input('Guess an x coordinate between 1 and 5: ')
    user_x = int(user_xstr) - 1
    guess_columns.append(user_x)
    return guess_columns


# Appends user x and y guesses into a list of coordinate tuples
guess_x = guess_column()
guess_y = guess_row()
for x, y in zip(guess_x, guess_y):
    user_guesses.append((x, y))

print(user_guesses)

# class Board:
#
#     def __init__(self, size, num_targets):
#         self.size = size
#         self.num_targets = num_targets
#         self.targets = []
#         self.guesses = []
