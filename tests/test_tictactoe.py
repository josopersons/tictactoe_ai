import unittest

from tictactoe_ai import TicTacToeAI


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        self.ai = TicTacToeAI()

    def test_solve_state(self):
        states = ["xexeoeeoe", "xexooxeee", "xoxxoeoxe", "xeeeeeeee",
                  "xeeeoeeex", "xxxeoeoee", "oooexexex", "xoxxoooxx",
                  "xxoeoxeee", "eeeeeeeee"]
        expected_results = ["win", "loss", "tie", "tie", "tie", "loss",
                            "loss", "tie", "win", "tie"]
        results = [self.ai.solve_state(s) for s in states]
        for i in range(len(expected_results)):
            self.assertEqual(expected_results[i], results[i], "For state: " +
                             states[i] + " Expected: " + expected_results[i] +
                             " Got: " + results[i])

    def test_get_move(self):
        states = ["xexeoeeoe", "xexooxeee", "xoxxoeoxe", "xeeeeeeee",
                  "xeeeoeeex", "xxxeoeoee", "oooexexex", "xoxxoooxx",
                  "eeeeeeeee"]
        expected_moves = [[(0, 1)],
                          [(0, 1)],
                          [(1, 2), (2, 2)],
                          [(1, 1)],
                          [(0, 1), (1, 0), (1, 2), (2, 1)],
                          [None],
                          [None],
                          [None],
                          [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
                           (2, 0), (2, 1), (2, 2)]]
        moves = [self.ai.get_move(s) for s in states]
        for i in range(len(expected_moves)):
            if moves[i] not in expected_moves[i]:
                self.assertTrue(False, "%s is not a correct move for state: "
                                % (moves[i],) + states[i])

if __name__ == "__main__":
    unittest.main()
