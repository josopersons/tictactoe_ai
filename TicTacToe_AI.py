class TicTacToeAI:

    """The dictionary solutions maps a board state to a result.
    The results are either 'win', 'loss' or 'tie'. The results are given
    in terms of the player who is next to move.
    """

    solutions = {}
    solved = False

    def solve(self):
        if not self.solved:
            self.solve_state("eeeeeeeee")
            self.solved = True

    def solve_state(self, state):
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
        children = []
        if self.end_result(state) == "incomplete":
            player = "x"
            if state.count("x") > state.count("o"):
                player = "o"
            for i in range(len(state)):
                if state[i] == "e":
                    new_state = state[:i] + player + state[i+1:]
                    children.append(new_state)
        return children

    def end_result(self, state):
        # returns incomplete loss tie
        victory = ["xxx", "ooo"]
        diagonal_one = ""
        diagonal_two = ""
        for i in range(3):
            horizontal = ""
            vertical = ""
            diagonal_one += state[i*3 + i]
            diagonal_two += state[i*2 + 2]   # i*3 + 2 - i
            for j in range(3):
                horizontal += state[i*3 + j]
                vertical += state[j*3 + i]
            if any(l in victory for l in (horizontal, vertical)):
                return "loss"
        if any(l in victory for l in (diagonal_one, diagonal_two)):
            return "loss"
        if state.count("e") == 0:
            return "tie"
        return "incomplete"

    def is_solved(self):
        return "eeeeeeeee" in self.solutions

    def get_move(self, state):
        """Operates under the assumption that this is the current game state
        and the next move requested is for the player who is about to make a move.
        Also assumes the current state is valid and that the game is not over.
        """
        if type(state) is not str:
            state = self.convert_state(state)
        if state not in self.solutions:
            self.solve_state(state)
        children = self.get_child_states(state)
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
        result = []
        for i in state:
            result.append("".join(i))
        return "".join(result)
