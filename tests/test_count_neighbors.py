import unittest
import numpy as np

from game_of_life import count_neighbors


class TestCountNeighbors(unittest.TestCase):

    def test_three_neighbors(self):

        board = np.array([
            [0,1,0],
            [1,1,0],
            [0,1,1]
        ], dtype=int)

        result = count_neighbors(board,1,1)

        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()

