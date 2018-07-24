class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        def dfs(queens, xy_sum, xy_diff):
            row = len(queens)
            if row == n:
                # completes
                solution = ['.'*col+'Q'+'.'*(n-col-1) for col in queens]
                ans.append(solution)
                return
                        
            for col in range(n):
                s = row+col
                d = row-col
                if col not in queens and s not in xy_sum and d not in xy_diff:
                    dfs(queens+[col], xy_sum+[s], xy_diff+[d])
        dfs([], [], [])
        return ans
