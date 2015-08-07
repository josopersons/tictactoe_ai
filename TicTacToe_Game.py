
"""This module contains the game logic for Tic Tac Toe.
Tic Tac Toe, played by two people on a 3x3 board.
"""


class TicTacToe():

    def __init__(self):
        self._board = self.create_board()
        self._turn = None
        self._finished = 'e'
        self._error = None

    def update(self, player, square):
        """Updates game state based on player and square.
        Expects:
            player -- The player symbol ('x'/'o').
            square -- The TicTacToe square the move is to be made on.
                      The coordinates should be accesible via (square[0], square[1]).
        Returns:
            "Success" -- If the move was made correctly
            The error made -- If the move was invalid
        """
        # checks validity of move
        if self.is_valid(player, square):
            # makes move, finishes turn, checks if the game is over
            self.mark_square(self._turn, square)
            self.finish_turn()
            self._finished = self.done()
            return "Success"
        else:
            return self._error

    def start(self):
        """Starts the game.
        The player with the symbol 'x' is set as the first to play.
        """
        self._turn = 'x'

    def done(self):
        """Checks if the game is complete.
        Returns:
            'e'     -- If the game is unfinished
            'x'/'o' -- For a player victory
            't'     -- If the game ends in a tie.
        """
        e = 'e'
        # returns x, o for victory, e for unfinished, and t for tie
        has_empty = False
        line_1 = set()
        line_2 = set()
        # check horizontals and verticals
        for i in range(3):
            for j in range(3):
                # check to see if board is filled
                if self._board[i][j] == e:
                    has_empty = True
                # horizontals
                line_1.add(self._board[i][j])
                # verticals
                line_2.add(self._board[j][i])
            # check lines for victory
            if self.check_line(line_1):
                return self.check_line(line_1)
            if self.check_line(line_2):
                return self.check_line(line_2)
            # clear and check next set
            line_1.clear()
            line_2.clear()
        # check diagonals
        for i in range(3):
            line_1.add(self._board[i][i])
            line_2.add(self._board[i][2 - i])
        if self.check_line(line_1):
            return self.check_line(line_1)
        if self.check_line(line_2):
            return self.check_line(line_2)
        # indicate whether or not the game is finished
        if has_empty:
            return 'e'
        else:
            return 't'

    def create_board(self):
        """Returns an empty 3x3 board
        The coordinates of each board space are (x, y), with the bottom left
        corner square as (0,0) and the top right corner square as (2,2).
        The board can be accessed through board[x][y].
        """
        e = 'e'
        return [[e, e, e], [e, e, e], [e, e, e]]

    # TODO: modify errors to a better format
    def is_valid(self, player, square):
        """Checks if a given move is valid
        Expects:
            square -- An object containing the coordinates of the board square.
                      The coordinates x, y should be accesible via square[0],
                      square[1] respectively.
            player -- The player symbol, either 'x' or 'o'
        """
        if self._finished != 'e':
            self._error = "This game is already finished"
            return False
        if player != self._turn:
            self._error = "It is not your turn"
            return False
        if self._board[square[0]][square[1]] != 'e':
            self._error = "This square is not empty"
            return False
        return True

    def mark_square(self, symbol, square):
        """Marks square with symbol"""
        self._board[square[0]][square[1]] = symbol

    def finish_turn(self):
        """Takes actions to finish a turn
        Turn passes from current player to other player"""
        if self._turn == 'x':
            self._turn = 'o'
        else:
            self._turn = 'x'

    def check_line(self, line):
        """Checks if a line on the board contains all x's or o's.
        Returns 'x'/'o' if it contains all 'x'/'o', None otherwise.
        """
        if 'e' not in line and 'o' not in line:
            return 'x'
        elif 'e' not in line and 'x' not in line:
            return 'o'
        else:
            return None

    def get_board(self):
        return self._board
