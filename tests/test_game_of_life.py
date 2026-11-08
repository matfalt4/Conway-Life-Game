import unittest
import numpy as np

from game_of_life import count_neighbors


class TestGameOfLife(unittest.TestCase):

    def test_corner_neighbors(self):

        board = np.zeros((3, 3), dtype=int)

        board[0, 1] = 1
        board[1, 0] = 1
        board[1, 1] = 1

        result = count_neighbors(board, 0, 0)

        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
