import unittest
import numpy as np

from game_of_life import new_generation


class TestNewGeneration(unittest.TestCase):

    def test_periodic_cond(self):

        board = np.array([
            [0,0,1],
            [0,0,1],
            [0,0,1]
        ], dtype=int)

        board = new_generation(board)

        self.assertEqual(board[1][0],1)


if __name__ == "__main__":
    unittest.main()
