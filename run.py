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
    "\n\nThere are enemy spacecraft all around us.\n"
    +
    "Shoot them with your lazer to eliminate the threat.\n\n"
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


def rand_row(board_size):
    rows = []
    target_row = 0
    for _ in range(3):
        target_row = randint(0, board_size)
        rows.append(target_row)
    return rows


def rand_col(board_size):
    cols = []
    target_col = 0
    for _ in range(3):
        target_col = randint(0, board_size)
        cols.append(target_col)
    return cols


rand_row(5)
rand_col(5)


def get_user_guess():
    guess_col = input('Guess a column between 1 and 5: ')
    while guess_col not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        guess_col = input('Guess a column between 1 and 5: ')

    guess_row = input('Guess a row between 1 and 5: ')
    while guess_row not in '12345':
        print('Invalid input. Choose a number between 1 and 5: ')
        guess_row = input('Guess a row between 1 and 5: ')

    return int(guess_col) - 1, int(guess_row) - 1


get_user_guess()
# if guess_row and guess_col

# class Board:
#     """
#     Defines a class for board in order to
#     access size of board and number of targets
#     according to difficulty.
#     With methods to add target position and
#     player guess when needed.
#     """

#     def __init__(self, size, num_targets):
#         self.size = size
#         self.num_targets = num_targets
#         self.board = ["✩" for x in range(size) for y in range(size)]
#         self.targets = []
#         self.guesses = []

#     def render_board(self):
#         for row in self.board:
#             print(" ".join(row))
