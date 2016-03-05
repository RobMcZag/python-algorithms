import Board
import heapq
import sys

class Node:
    def __init__(self, board, move, prev):
        self.board = board  # Board object, not only the tiles
        self.move = move
        self.prev = prev

    def manhattan(self):
        return self.move + self.board.manhattan()


class Solver:
    def __init__(self, board):
        startNode = Node(board, 0, None)
        startTwinNode = Node(board.twin(), 0, None)

        solNode = self.solveManhattan(startNode, startTwinNode)

        node = solNode
        self.solution = []

        while node != None:
            self.solution.insert(0, node.board) # the Board object
            node = node.prev



    def solveManhattan(self, startNode, startTwinNode):
        pq = []
        heapq.heappush(pq, (startNode.manhattan(), startNode))
        pqTwin = []
        heapq.heappush(pqTwin, (startTwinNode.manhattan(), startTwinNode))

        while True:
            (m, node) = heapq.heappop(pq)
            (mt, nodeTwin) = heapq.heappop(pqTwin)

            if node.board.isgoal() or nodeTwin.board.isgoal():
                break

            self.addNeighbours(node, pq)
            self.addNeighbours(nodeTwin, pqTwin)

        if node.board.isgoal(): return node
        return None


    def addNeighbours(self, node, pq):
        for board in node.board.neighbors():
            if node.prev == None or board != node.prev.board:
                n = Node(board, node.move + 1, node)
                heapq.heappush(pq, (n.manhattan(), n))

    def isSolvable(self):
        return len(self.solution) > 0

    def moves(self):
        return len(self.solution) -1

def main(args):
    fh = open(args[1])

    l = fh.readline()
    N = int(l.strip())

    board = []
    for line in fh:
        for word in line.split():
            board.append(int(word))

    solver = Solver(Board.Board(board, N))

    if not solver.isSolvable():
      print "No solution possible"
    else:
      print "Minimum number of moves = ", solver.moves()
      for board in solver.solution:
        print board.toString()
      print "Minimum number of moves = ", solver.moves()


main(sys.argv)
