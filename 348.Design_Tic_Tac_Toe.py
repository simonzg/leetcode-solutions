# time complexity for move: O(1)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        #self.board = [[0]*n for i in range(n)]
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.backDiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        v = 1 if player == 1 else -1
        r, c = row, col
        #self.board[r][c] = v
        self.rows[r] += v
        self.cols[c] += v
        if r == c:
            self.diag += v
        if r == self.n-1-c:
            self.backDiag += v
        for val in [self.rows[r], self.cols[c], self.diag, self.backDiag]:
            if val == -self.n:
                return 2
            elif val == self.n:
                return 1
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
