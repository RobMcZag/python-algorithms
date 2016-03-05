
class Board:

    ROW_COL_BASE = 1

    def __init__(self, board, N):
        """
        Builds a Board from a list of blocks and the size of the board. The list must hold N^2 blocks.

        :param board: the list with the blocks.
        :param N: the size of the board (length = width = N)
        :return: a new Board with the blocks setup as passed.
        """
        self.board = board
        self.N = N

    @classmethod
    def fromMatrix(cls, blocks):
        """
        Builds a Board from a matrix of blocks, i.e. from a list of list of blocks.

        :param blocks: the matrix with the blocks
        :return: a new Board with the blocks setup as passed.
        """
        l = []
        for row in blocks:
            for block in row:
                l.append(block)
        N = len(row)
        return cls(l, N)

    def dimension(self):
        """ board dimension N """
        return self.N


#    public int hamming()
    #  number of blocks out of place

    def manhattan(self):
        '''
        :return: the sum of Manhattan distances between blocks and goal
        '''
        manhval = 0
        for idx, tile in enumerate(self.board):
            if tile == 0: continue
            rm = (tile -1) / self.N - idx / self.N
            cm = (tile -1) % self.N - idx % self.N
            manhval += abs(rm) + abs(cm)
        return manhval

    def isgoal(self):
        '''
        is this board the goal board?

         :return: a boolean, true if this board is the goal board
        '''
        NN = self.N * self.N
        for idx, val in enumerate(self.board):
            if (idx != (NN-1) and val != idx +1):
                return False
        return True

    def _index(self, row, col):
        return self.N * (row - self.ROW_COL_BASE) + (col - self.ROW_COL_BASE)

    def twin(self):
        """
        a board that is obtained by exchanging any pair of blocks
        :return: Board
        """
        twin = self.board[:]

        idx11 = self._index(1, 1)
        idx12 = self._index(1, 2)
        idx21 = self._index(2, 1)
        idx22 = self._index(2, 2)

        if (twin[idx11] == 0):
          twin[idx12] = self.board[idx22] # 0 A
          twin[idx22] = self.board[idx12] # x B
        else:
              if (twin[idx12] == 0):
                twin[idx11] = self.board[idx21] # A 0
                twin[idx21] = self.board[idx11] # B x
              else:
                twin[idx11] = self.board[idx12] # A B
                twin[idx12] = self.board[idx11] ## ? ?
        return Board(twin, self.N);

    def neighbors(self):
        """
        all neighboring boards

        :return: a list of neighbours Boards
        """

        blankidx = self.board.index(0)
        brow = blankidx / self.N
        bcol = blankidx % self.N
        idx0 = self._index(brow + 1, bcol + 1)

        nbrs = []

        if brow > 0:    # move space up
            nbrs.append(self._neighborBoard(brow, bcol + 1, idx0))

        if brow < self.N - 1:    # move space down
            nbrs.append(self._neighborBoard(brow + 2, bcol + 1, idx0))

        if bcol > 0:    # move space left
            nbrs.append(self._neighborBoard(brow + 1, bcol, idx0))

        if bcol < self.N - 1:    # move space right
            nbrs.append(self._neighborBoard(brow + 1, bcol + 2, idx0))

        return nbrs

    def _neighborBoard(self, brow, bcol, idx0):
        idxdst = self._index(brow, bcol)  # +1 is for 1 based row and cols
        brd = self.board[:]
        brd[idx0] = self.board[idxdst];
        brd[idxdst] = self.board[idx0];
        b = Board(brd, self.N)
        return b

    def __eq__(self, other):
        if other is None: return False
        if other is self: return True
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        if other is None: return True
        return not self.__eq__(other)

    def toString(self):
        """
        :return: the string representation of this board.
        """
        s = '{N}\n'.format(N = self.N)
        for idx, val in enumerate(self.board):
            s += '{0:2d}'.format(val)
            if ((idx + 1) % self.N) == 0: s += '\n'
        return s


#    public static void main(String[] args) // unit tests (not graded)
