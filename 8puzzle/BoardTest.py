import unittest
import Board

class BoardTest(unittest.TestCase):

    def testCreateFromList(self):
        b = Board.Board([1, 2, 3, 0], 2)
        self.assertEqual(b.board, [1, 2, 3, 0])
        self.assertEqual(b.N, 2)

    def testCreateFromMatrix(self):
        b = Board.Board.fromMatrix([[1, 2], [3, 0]])
        self.assertEqual(b.board, [1, 2, 3, 0])
        self.assertEqual(b.N, 2)
        self.assertEqual(b.dimension(), 2)

    def testIsGoal(self):
        b = Board.Board([1, 2, 3, 0], 2)
        self.assertTrue(b.isgoal())

    def testManhattan1(self):
        b = Board.Board([1, 2, 3, 0], 2)
        self.assertEqual(b.manhattan(), 0)

    def testManhattan2(self):
        b = Board.Board([1, 2, 0, 3], 2)
        self.assertEqual(b.manhattan(), 1)

    def testManhattan3(self):
        b = Board.Board([8, 1, 3, 4, 0, 2, 7, 6, 5], 3)
        self.assertEqual(b.manhattan(), 10)

    def testTwin1(self):
        b = Board.Board([1, 2, 0, 3], 2)
        self.assertEqual(b.twin().board, [2, 1, 0, 3])

    def testTwin2(self):
        b = Board.Board([0, 2, 1, 3], 2)
        self.assertEqual(b.twin().board, [0, 3, 1, 2])

    def testTwin3(self):
        b = Board.Board([1, 0, 2, 3], 2)
        self.assertEqual(b.twin().board, [2, 0, 1, 3])

    def testNeighbors1(self):
        b = Board.Board([1, 0, 2, 3], 2)
        self.assertEqual(len(b.neighbors()), 2)

    def testNeighbors2(self):
        b = Board.Board([8, 1, 3, 4, 0, 2, 7, 6, 5], 3)
        self.assertEqual(len(b.neighbors()), 4)

    def testNeighbors3(self):
        b = Board.Board([8, 1, 3, 4, 2, 0, 7, 6, 5], 3)
        self.assertEqual(len(b.neighbors()), 3)

    def testNeighbors4(self):
        b = Board.Board([8, 1, 0, 4, 2, 3, 7, 6, 5], 3)
        self.assertEqual(len(b.neighbors()), 2)

    def testToString1(self):
        b = Board.Board([1, 0, 2, 3], 2)
        self.assertEqual(b.toString(), '2\n 1 0\n 2 3\n')

    def testToString2(self):
        b = Board.Board([8, 1, 0, 4, 2, 3, 7, 6, 5], 3)
        self.assertEqual(b.toString(), '3\n 8 1 0\n 4 2 3\n 7 6 5\n')

if __name__ == '__main__':
    unittest.main()
