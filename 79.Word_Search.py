class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m,n = len(board), len(board[0])
        
        def find(word, start):
            if not word:
                return True
            i,j = start
            value = board[i][j]
            board[i][j] = '#'
            
            for (r,c) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=r<=m-1 and 0<=c<=n-1 and board[r][c] == word[0]:
                    if find(word[1:], (r,c)):
                        return True
            board[i][j] = value
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(word[1:], (i,j)):
                        return True
        return False
