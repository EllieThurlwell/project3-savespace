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
    board = []

    for _ in range(board_size):
        board.append(['.'] * board_size)

    for row in board:
        print(" ".join(row))


def rand_row(board_size):
    return randint(0, board_size)


def rand_col(board_size):
    return randint(0, board_size)


target_row = rand_row(5)
target_col = rand_col(5)

guess_row = int(input('Guess a row: '))
guess_col = int(input('Guess a column: '))

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
