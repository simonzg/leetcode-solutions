# Solution with O()
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
    def findUnassigned(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return (i,j)
        return (-1,-1)
    
    def solve(self):
        i,j = self.findUnassigned()
        if i == -1 and j == -1:
            return True
        for d in self.getPossibleDigits(i,j):
            self.board[i][j] = d
            if self.solve():
                return True
            self.board[i][j] = '.'
        return False
    
    def getPossibleDigits(self, row, col):
        digits = '1,2,3,4,5,6,7,8,9'.split(',')
        collision = set([])
        for i in range(9):
            if self.board[row][i] != '.':
                collision.add(self.board[row][i])
            if self.board[i][col] != '.':
                collision.add(self.board[i][col])
        r3 = row//3
        c3 = col//3
        rowLimit = range(r3*3, (r3+1)*3)
        colLimit = range(c3*3, (c3+1)*3)
        for i in rowLimit:
            for j in colLimit:
                if self.board[i][j] != '.':
                    collision.add(self.board[i][j])
        for d in collision:
            digits.remove(d)
        return digits
    
