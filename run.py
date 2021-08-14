# Save Space battleships style game

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

board = []

# board size 5
for i in range(0, 5):
    board.append(['.'] * 5)


def print_board(board_width, board_height):
    """
    prints the board for the user to play against
    """
    # top_bot = ' ✮ ' * (board_width + 2)
    # print(top_bot)
    # for row in range(board_height):
    #     print(' ✮ ' + ' . ' * board_width + ' ✮ ')
    # print(top_bot)
    for row in board:
        print(" ".join(row))


print_board(5, 5)


class Board:
    """
    Defines a class for board in order to
    access size of board and number of targets
    according to difficulty.
    With methods to add target position and
    player guess when needed.
    """

    def __init__(self, size, num_targets):
        self.size = size
        self.num_targets = num_targets
        self.board  # for i in range size ?
        self.targets = []
        self.guesses = []
