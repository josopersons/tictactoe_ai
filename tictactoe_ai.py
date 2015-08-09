class TicTacToeAI:

    """The dictionary solutions maps a board state to a result.
    The results are either 'win', 'loss' or 'tie'. The results are given
    in terms of the player who is next to move.

    All states are represented by a nine character string, with 'e'
    indicating and empty space, and 'x'/'o' indicating the respective
    tic tac toe symbols.

    A valid state is one reachable without breaking any rules of tic tac toe,
    or playing past the endgame.
    """

    solutions = {}
    solved = False

    def solve(self):
        """Solves all possible valid states to determine whether the state
        will lead to a win, loss or tie.
        """
        if not self.solved:
            self.solve_state("eeeeeeeee")
            self.solved = True

    def solve_state(self, state):
        """Solves state given. Will also solve all child states of this state.
        Win/loss for a state always given in terms of player who should go
        next.

        Expects:
            state -- String representation of game state.

        Returns:
            "win"/"loss"/"tie" -- The result of the game if played optimally
                                  from this state.
        """
        if state not in self.solutions:
            result = "loss"
            children = self.get_child_states(state)
            if children:
                predictions = [self.solve_state(child) for child in children]
                if "loss" in predictions:
                    result = "win"
                elif "tie" in predictions:
                    result = "tie"
            else:
                result = self.end_result(state)
            self.solutions[state] = result
        return self.solutions[state]

    def get_child_states(self, state):
        """Finds all the states that can be reached from the current state
        with one move.

        Expects:
            state -- String representation of game state. State must be valid.

        Returns:
            List of child states
            Empty list -- If the state is one with no more moves to be made
                          it has no child states.
        """
        children = []
        if self.end_result(state) == "incomplete":
            player = "x"
            if state.count("x") > state.count("o"):
                player = "o"
            for i in range(len(state)):
                if state[i] == "e":
                    new_state = state[:i] + player + state[i + 1:]
                    children.append(new_state)
        return children

    def end_result(self, state):
        """Checks whether the game is complete and returns the state of
        the game.

        Expects:
            state -- String representation of game state. State must be
                     valid.

        Returns:
            "incomplete" -- If the game is not finished yet.
            "tie"        -- If the game has finished and the result is a tie.
            "loss"       -- If the game has finished and a player has won/lost.
                            The next move would have belonged to the player
                            who has lost, ergo the state is recorded as a loss.
        """
        victory = ["xxx", "ooo"]
        diagonal_one = ""
        diagonal_two = ""
        for i in range(3):
            horizontal = ""
            vertical = ""
            diagonal_one += state[i * 3 + i]
            diagonal_two += state[i * 2 + 2]   # i*3 + 2 - i
            for j in range(3):
                horizontal += state[i * 3 + j]
                vertical += state[j * 3 + i]
            if any(l in victory for l in (horizontal, vertical)):
                return "loss"
        if any(l in victory for l in (diagonal_one, diagonal_two)):
            return "loss"
        if state.count("e") == 0:
            return "tie"
        return "incomplete"

    def is_solved(self):
        """Checks whether the full game has been solved.
        """
        return "eeeeeeeee" in self.solutions

    def get_move(self, state):
        """Operates under the assumption that this is the current game state
        and the next move requested is for the player who is about to make a
        move.

        Expects:
            state -- String representation of game state or 2-D array
                     representation of game state. State must be valid.

        Returns:
            move -- A tuple containing the coordinates of square on the
                    tic tac toe board. Coordinates are such that the top left
                    square is (0, 0) and the bottom right square is (2, 2).
        """
        if type(state) is not str:
            state = self.convert_state(state)
        if state not in self.solutions:
            self.solve_state(state)
        children = self.get_child_states(state)
        if not children:
            return None
        move_state = None
        for child in children:
            if self.solutions[child] == "loss":
                move_state = child
            elif not move_state and self.solutions[child] == "tie":
                move_state = child
        # This should never happen if the AI is working properly
        if not move_state:
            move_state = children[0]
        # The move is in board coordinates
        moves = [i for i in range(len(state)) if state[i] != move_state[i]]
        move = (moves[0] // 3, moves[0] % 3)
        return move

    def convert_state(self, state):
        """Converts a 2-D array state into a string state.

        Expects:
            state -- A 2-D array representing game state.

        Returns:
            Game state represented as a string
        """
        result = []
        for i in state:
            result.append("".join(i))
        return "".join(result)
