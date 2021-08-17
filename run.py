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


def print_board(board_size):
    """
    prints the board for the user to play against
    """
    board = []

    for _ in range(board_size):
        board.append(['.'] * board_size)

    for row in board:
        print("  ".join(row))


print_board(5)


def get_user_guesses():
    """
    request user to input a row and column value
    check if input is valid
    """
    user_xstr = input('\nGuess an x coordinate between 1 and 5: ')
    while user_xstr not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        user_xstr = input('\nGuess a column between 1 and 5: ')
    guess_columns = []
    user_x = int(user_xstr) - 1
    guess_columns.append(user_x)

    user_ystr = input('\nGuess a y coordinate between 1 and 5: ')
    while user_ystr not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        user_ystr = input('\nGuess a row between 1 and 5: ')
    guess_rows = []
    user_y = int(user_ystr) - 1
    guess_rows.append(user_y)

    user_guesses = []

    for x, y in zip(guess_columns, guess_rows):
        user_guesses.append((x, y))

    print(user_guesses)


get_user_guesses()

# def get_eight_guesses():
#     chance = 1
#     while chance <= 8:
#         print(f'Chance {chance}')
#         guess_column()
#         guess_row()
#         chance += 1
#         if chance > 8:
#             print('Out of chances!')
#             break


# user_guesses = []


# def guess_row():
#     """
#     Takes user input for y coordinate value and
#     appends it to a list of y values, taking into
#     account zero-based indexing
#     """
#     guess_rows = []
#     user_ystr = input('Guess a y coordinate between 1 and 5: ')
#     user_y = int(user_ystr) - 1
#     guess_rows.append(user_y)
#     return guess_rows


# def guess_column():
#     """
#     Takes user input for x coordinate value and
#     appends it to a list of x values, taking into
#     account zero-based indexing
#     """
#     guess_columns = []
#     user_xstr = input('Guess an x coordinate between 1 and 5: ')
#     user_x = int(user_xstr) - 1
#     guess_columns.append(user_x)
#     return guess_columns


# get_eight_guesses()


# # Appends user x and y guesses into a list of coordinate tuples
# guess_x = guess_column()
# guess_y = guess_row()
# for x, y in zip(guess_x, guess_y):
#     user_guesses.append((x, y))


# print(user_guesses)
