class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(queens, xy_sum, xy_diff):
            row = len(queens)
            if row == n:
                return 1
            count = 0
            for col in range(n):
                _sum = row+col
                diff = row-col
                if col not in queens and _sum not in xy_sum and diff not in xy_diff:
                    count += dfs(queens+[col], xy_sum+[_sum], xy_diff+[diff])
            return count     
        return dfs([],[],[])
