class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        dic = {}
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cur = board[i][j]
                square = [(i-1,j-1),(i,j-1),(i+1,j-1),(i+1,j+1),(i,j+1),(i-1,j+1), (i-1,j),(i+1,j)]
                total = 0
                for r,c in square:
                    if 0<=r<m and 0<=c<n:
                        total += board[r][c]
                nxt = 0
                if (cur==1 and 2<=total<=3) or (cur==0 and total==3):
                    nxt = 1
                if nxt != cur:
                    dic[i,j] = nxt
                
        for (i,j) in dic:
            board[i][j] = dic[i,j]
                    