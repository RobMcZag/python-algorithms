import unittest
import Solver, Board

class SolverTest(unittest.TestCase):

    def testSolveGoal(self):
        # b = Board.Board([8, 1, 0, 4, 2, 3, 7, 6, 5], 3)
        b = Board.Board([1, 2, 3, 0], 2)
        s = Solver.Solver(b)
        self.assertEqual(s.isSolvable(), True)
        self.assertEqual(s.moves(), 0)
        # for s in [ b.toString() for b in s.solution]:
        #     print s

    def testSolve2(self):
        # b = Board.Board([8, 1, 0, 4, 2, 3, 7, 6, 5], 3)
        b = Board.Board([3, 1, 0, 2], 2)
        s = Solver.Solver(b)
        self.assertEqual(s.isSolvable(), True)
        self.assertEqual(s.moves(), 3)
        # for s in [ b.toString() for b in s.solution]:
        #     print s

if __name__ == '__main__':
    unittest.main()
