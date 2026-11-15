import unittest
import numpy as np

from game_of_life import new_generation


class TestIfDead(unittest.TestCase):

    def test_if_dead(self):

        board = np.array([
            [0,0,0],
            [0,1,1],
            [0,0,0]
        ], dtype=int)

        board = new_generation(board)

        self.assertEqual(board[1][1], 0)


if __name__ == "__main__":
    unittest.main()
